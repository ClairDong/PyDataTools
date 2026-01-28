"""
线性回归核心计算模块
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def linear_regression_from_csv(csv_file):
    """
    读取指定的CSV文件并执行线性回归
    
    参数:
        csv_file: CSV文件路径或文件对象，应包含'X'和'Y'两列
    
    返回:
        slope: 回归系数（斜率）
        intercept: 截距
        r_squared: R²决定系数（评估模型拟合度）
        predictions: 预测值（numpy数组）
        X: 特征数据（numpy数组）
        Y: 目标数据（numpy数组）
    """
    # 如果是文件对象，重置文件指针到开头
    if hasattr(csv_file, 'seek'):
        csv_file.seek(0)
    
    # 读取CSV文件（支持文件路径或文件对象）
    try:
        df = pd.read_csv(csv_file, encoding='utf-8-sig')
    except pd.errors.EmptyDataError:
        raise ValueError("CSV文件为空，请检查文件内容")
    except Exception as e:
        raise ValueError(f"读取CSV文件时出错: {str(e)}")
    
    # 检查数据框是否为空
    if df.empty:
        raise ValueError("CSV文件没有数据行，请确保文件包含数据")
    
    # 检查必要的列是否存在
    if 'X' not in df.columns or 'Y' not in df.columns:
        raise ValueError("CSV文件必须包含'X'和'Y'两列")
    
    # 提取X和Y数据
    X = df['X'].values.reshape(-1, 1)  # 转换为列向量
    Y = df['Y'].values
    
    # 创建线性回归模型
    model = LinearRegression()
    
    # 训练模型
    model.fit(X, Y)
    
    # 获取回归系数和截距
    slope = model.coef_[0]
    intercept = model.intercept_
    
    # 计算预测值
    predictions = model.predict(X)
    
    # 计算R²决定系数
    r_squared = model.score(X, Y)
    
    return slope, intercept, r_squared, predictions, X.flatten(), Y
