"""
PyDataTools - Python数据处理工具
主应用入口，整合所有功能模块
"""
import sys
import os

# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import streamlit as st
from app.config import PAGE_CONFIG
from modules.regression.web_ui import regression_page

# 页面配置
st.set_page_config(**PAGE_CONFIG)

# 侧边栏导航
st.sidebar.title("📊 PyDataTools")
st.sidebar.markdown("---")

page = st.sidebar.selectbox(
    "选择功能模块",
    ["线性回归", "参数拟合", "矩阵运算"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    **PyDataTools** 是一个基于 Streamlit 的数据处理工具集，
    提供多种数据分析和处理功能。
    """
)

# 路由到对应页面
if page == "线性回归":
    regression_page()
elif page == "参数拟合":
    st.title("🔧 参数拟合")
    st.info("🚧 参数拟合功能开发中，敬请期待...")
    st.markdown("""
    ### 计划功能
    - 非线性函数拟合
    - 多项式拟合
    - 自定义函数拟合
    """)
elif page == "矩阵运算":
    st.title("🔢 矩阵运算")
    st.info("🚧 矩阵运算功能开发中，敬请期待...")
    st.markdown("""
    ### 计划功能
    - 矩阵加减乘除
    - 矩阵求逆
    - 特征值与特征向量
    - 矩阵分解
    """)

# 页脚
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "PyDataTools - Python数据处理工具 | 使用 Streamlit 构建"
    "</div>",
    unsafe_allow_html=True
)
