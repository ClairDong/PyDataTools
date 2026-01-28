"""
线性回归模块的Web界面组件
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io
from modules.regression.core import linear_regression_from_csv
from utils.visualization import setup_chinese_font, get_label, CHINESE_FONT_AVAILABLE
from utils.file_handler import validate_csv_file, validate_regression_columns

# 配置matplotlib支持中文显示
setup_chinese_font()


def regression_page():
    """
    线性回归功能页面
    """
    st.title("📊 单线性回归分析工具")
    st.markdown("---")
    
    # 侧边栏说明
    with st.sidebar:
        st.header("📖 使用说明")
        st.markdown("""
        1. **上传CSV文件**：文件应包含 'X' 和 'Y' 两列
        2. **查看结果**：程序会自动进行线性回归分析
        3. **下载结果**：可以下载回归结果图像
        """)
        st.markdown("---")
        st.markdown("**示例数据格式：**")
        st.code("""
        X,Y
        1.0,2.5
        2.0,4.8
        3.0,7.2
        """)
    
    # 文件上传
    uploaded_file = st.file_uploader(
        "选择CSV文件",
        type=['csv'],
        help="请上传包含X和Y两列的CSV文件"
    )
    
    if uploaded_file is not None:
        try:
            # 验证CSV文件
            df = validate_csv_file(uploaded_file)
            if df is None:
                st.stop()
            
            # 显示数据预览
            st.subheader("📋 数据预览")
            st.dataframe(df.head(10), use_container_width=True)
            st.info(f"数据总行数: {len(df)} 行")
            
            # 验证列
            if not validate_regression_columns(df):
                st.stop()
            
            # 重置文件指针以便regression模块读取
            uploaded_file.seek(0)
            
            # 执行线性回归
            with st.spinner("正在进行线性回归分析..."):
                slope, intercept, r_squared, predictions, X, Y = linear_regression_from_csv(uploaded_file)
            
            # 创建两列布局
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.subheader("📈 回归结果")
                # 显示结果指标
                st.metric("斜率", f"{slope:.4f}")
                st.metric("截距", f"{intercept:.4f}")
                st.metric("决定系数 (R²)", f"{r_squared:.4f}")
                
                # 显示回归方程
                st.markdown("---")
                st.markdown("**回归方程：**")
                if intercept >= 0:
                    equation = f"Y = {slope:.4f}X + {intercept:.4f}"
                else:
                    equation = f"Y = {slope:.4f}X - {abs(intercept):.4f}"
                st.code(equation, language='text')
                
                # 模型评估
                st.markdown("---")
                st.markdown("**模型评估：**")
                if r_squared >= 0.9:
                    st.success(f"✅ 模型拟合度优秀 (R² = {r_squared:.4f})")
                elif r_squared >= 0.7:
                    st.warning(f"⚠️ 模型拟合度良好 (R² = {r_squared:.4f})")
                else:
                    st.info(f"ℹ️ 模型拟合度一般 (R² = {r_squared:.4f})")
            
            with col2:
                st.subheader("📊 可视化结果")
                # 创建图形
                fig, ax = plt.subplots(figsize=(10, 6))
                
                # 根据字体支持情况选择标签
                data_label = get_label('原始数据点', 'Data Points')
                reg_label = get_label('回归线', 'Regression Line')
                xlabel = get_label('X (特征变量)', 'X (Feature Variable)')
                ylabel = get_label('Y (目标变量)', 'Y (Target Variable)')
                title = get_label('单线性回归结果', 'Linear Regression Result')
                
                # 绘制原始数据点
                ax.scatter(X, Y, alpha=0.6, label=data_label, color='blue', s=50)
                
                # 绘制回归线（排序以便绘制平滑的线）
                sorted_indices = X.argsort()
                X_sorted = X[sorted_indices]
                predictions_sorted = predictions[sorted_indices]
                
                ax.plot(X_sorted, predictions_sorted, color='red', linewidth=2, 
                       label=f'{reg_label}: Y = {slope:.2f}X + {intercept:.2f}')
                
                # 设置图形属性
                ax.set_xlabel(xlabel, fontsize=12)
                ax.set_ylabel(ylabel, fontsize=12)
                ax.set_title(title, fontsize=14, fontweight='bold')
                ax.legend(fontsize=10)
                ax.grid(True, alpha=0.3)
                
                # 在图上添加文本信息
                if CHINESE_FONT_AVAILABLE:
                    info_text = f'斜率: {slope:.4f}\n截距: {intercept:.4f}\n决定系数(R²): {r_squared:.4f}'
                else:
                    info_text = f'Slope: {slope:.4f}\nIntercept: {intercept:.4f}\nR²: {r_squared:.4f}'
                ax.text(0.02, 0.98, info_text, transform=ax.transAxes,
                       fontsize=10, verticalalignment='top',
                       bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
                
                plt.tight_layout()
                st.pyplot(fig)
                
                # 下载图像按钮
                buf = io.BytesIO()
                plt.savefig(buf, format='png', dpi=150, bbox_inches='tight')
                buf.seek(0)
                st.download_button(
                    label="📥 下载图像",
                    data=buf,
                    file_name="regression_result.png",
                    mime="image/png"
                )
                plt.close()
            
            # 详细结果表格
            st.markdown("---")
            st.subheader("📊 详细数据")
            
            # 创建结果数据框
            results_df = pd.DataFrame({
                'X': X,
                'Y_实际值': Y,
                'Y_预测值': predictions,
                '残差': Y - predictions
            })
            st.dataframe(results_df, use_container_width=True)
            
            # 统计信息
            col3, col4, col5 = st.columns(3)
            with col3:
                st.metric("平均残差", f"{np.mean(Y - predictions):.4f}")
            with col4:
                st.metric("残差标准差", f"{np.std(Y - predictions):.4f}")
            with col5:
                st.metric("最大残差", f"{np.max(np.abs(Y - predictions)):.4f}")
            
        except Exception as e:
            st.error(f"❌ 发生错误: {str(e)}")
            st.exception(e)
    else:
        # 显示示例数据下载
        st.info("👆 请上传CSV文件开始分析，或下载示例数据")
        
        # 生成示例数据供下载
        if st.button("📥 下载示例数据"):
            np.random.seed(42)
            X_sample = np.random.uniform(0, 100, 100)
            Y_sample = 2 * X_sample + 30 + np.random.normal(0, 10, 100)
            sample_df = pd.DataFrame({'X': X_sample, 'Y': Y_sample})
            csv = sample_df.to_csv(index=False, encoding='utf-8-sig')
            st.download_button(
                label="下载示例CSV文件",
                data=csv,
                file_name="sample_data.csv",
                mime="text/csv"
            )
