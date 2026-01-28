"""
文件处理工具
处理文件上传、下载等功能
"""
import pandas as pd
import streamlit as st


def validate_csv_file(uploaded_file):
    """
    验证上传的CSV文件
    
    参数:
        uploaded_file: Streamlit上传的文件对象
    
    返回:
        df: 验证通过的数据框，如果验证失败则返回None并显示错误
    """
    if uploaded_file is None:
        return None
    
    # 重置文件指针到开头
    uploaded_file.seek(0)
    
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8-sig')
    except pd.errors.EmptyDataError:
        st.error("❌ 错误：CSV文件为空，请检查文件内容！")
        st.info("💡 提示：请确保CSV文件包含表头和数据行，格式如下：")
        st.code("X,Y\n1.0,2.5\n2.0,4.8\n3.0,7.2", language='csv')
        return None
    except Exception as e:
        st.error(f"❌ 读取CSV文件时出错: {str(e)}")
        return None
    
    # 检查数据框是否为空
    if df.empty:
        st.error("❌ 错误：CSV文件没有数据行！")
        st.info("💡 提示：请确保CSV文件包含数据行，格式如下：")
        st.code("X,Y\n1.0,2.5\n2.0,4.8\n3.0,7.2", language='csv')
        return None
    
    return df


def validate_regression_columns(df):
    """
    验证数据框是否包含线性回归所需的列（X和Y）
    
    参数:
        df: 数据框
    
    返回:
        bool: 验证是否通过
    """
    if 'X' not in df.columns or 'Y' not in df.columns:
        st.error("❌ 错误：CSV文件必须包含 'X' 和 'Y' 两列！")
        st.info(f"💡 当前文件的列名: {', '.join(df.columns.tolist())}")
        st.info("💡 提示：请确保CSV文件的第一行包含列名 'X' 和 'Y'")
        return False
    
    # 检查数据是否有效（不能全是NaN）
    if df['X'].isna().all() or df['Y'].isna().all():
        st.error("❌ 错误：X或Y列的数据全部为空！")
        return False
    
    return True
