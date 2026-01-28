"""
线性回归绘图模块
"""
import matplotlib
matplotlib.use('Agg')  # 使用非交互式后端，适合服务器环境
import matplotlib.pyplot as plt
from modules.regression.core import linear_regression_from_csv
from utils.visualization import setup_chinese_font

# 配置matplotlib支持中文显示
setup_chinese_font()


def plot_regression_results(csv_file, output_image='regression_result.png'):
    """
    读取CSV文件，调用回归函数，绘制结果并显示中文信息
    
    参数:
        csv_file: CSV文件路径
        output_image: 输出图像文件名，默认'regression_result.png'
    """
    # 调用回归函数
    slope, intercept, r_squared, predictions, X, Y = linear_regression_from_csv(csv_file)
    
    # 创建图形
    plt.figure(figsize=(10, 6))
    
    # 绘制原始数据点
    plt.scatter(X, Y, alpha=0.6, label='原始数据点', color='blue', s=50)
    
    # 绘制回归线（需要排序以便绘制平滑的线）
    sorted_indices = X.argsort()
    X_sorted = X[sorted_indices]
    predictions_sorted = predictions[sorted_indices]
    
    plt.plot(X_sorted, predictions_sorted, color='red', linewidth=2, 
             label=f'回归线: Y = {slope:.2f}X + {intercept:.2f}')
    
    # 设置图形属性（使用中文）
    plt.xlabel('X (特征变量)', fontsize=12)
    plt.ylabel('Y (目标变量)', fontsize=12)
    plt.title('单线性回归结果', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    
    # 在图上添加文本信息（中文）
    info_text = f'斜率: {slope:.4f}\n截距: {intercept:.4f}\n决定系数(R²): {r_squared:.4f}'
    plt.text(0.02, 0.98, info_text, transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    # 保存图形
    plt.tight_layout()
    plt.savefig(output_image, dpi=150, bbox_inches='tight')
    print(f"图像已保存为: {output_image}")
    plt.close()  # 关闭图形以释放内存
    
    # 打印结果（中文）
    print("\n" + "="*50)
    print("线性回归结果:")
    print("="*50)
    print(f"斜率: {slope:.4f}")
    print(f"截距: {intercept:.4f}")
    print(f"决定系数(R²): {r_squared:.4f}")
    print("="*50)


if __name__ == "__main__":
    # 读取CSV并绘制结果
    csv_file = 'data.csv'
    try:
        plot_regression_results(csv_file)
        print("\n程序执行完成！")
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{csv_file}'，请先运行 generate_data.py 生成数据")
    except Exception as e:
        print(f"错误: {e}")
