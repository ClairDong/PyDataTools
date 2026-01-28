"""
字体设置脚本
用于在Streamlit Cloud上安装中文字体支持
"""
import subprocess
import sys
import os

def install_fonts():
    """安装中文字体支持"""
    try:
        # 尝试安装文泉驿字体（免费开源中文字体）
        # 注意：这需要系统权限，在Streamlit Cloud上可能不可用
        subprocess.check_call([
            'apt-get', 'update', '-qq'
        ], stderr=subprocess.DEVNULL)
        
        subprocess.check_call([
            'apt-get', 'install', '-y', '-qq',
            'fonts-wqy-microhei',
            'fonts-wqy-zenhei'
        ], stderr=subprocess.DEVNULL)
        
        print("中文字体安装成功")
        return True
    except Exception as e:
        print(f"字体安装失败: {e}")
        return False

if __name__ == "__main__":
    install_fonts()
