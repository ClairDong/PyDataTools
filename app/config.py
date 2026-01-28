"""
应用配置文件
统一管理应用的主题、字体等配置
"""
from utils.visualization import setup_chinese_font

# 配置matplotlib支持中文显示
setup_chinese_font()

# Streamlit页面配置
PAGE_CONFIG = {
    'page_title': 'PyDataTools - Python数据处理工具',
    'page_icon': '📊',
    'layout': 'wide'
}
