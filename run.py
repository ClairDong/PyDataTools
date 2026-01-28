"""
PyDataTools 启动脚本
简化启动命令：python run.py
"""
import subprocess
import sys
import os

if __name__ == "__main__":
    # 确保在项目根目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # 启动Streamlit应用
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app/main.py"])
