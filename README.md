# PyDataTools - Python数据处理工具

PyDataTools 是一个基于 Streamlit 的 Web 应用，提供多种数据分析和处理功能。

## 功能特点

### 已实现功能
- 📊 **单线性回归分析** - 支持CSV文件上传，自动进行线性回归分析并可视化结果

### 计划功能
- 🔧 **参数拟合** - 非线性函数拟合、多项式拟合等
- 🔢 **矩阵运算** - 矩阵加减乘除、求逆、特征值分解等

## 项目结构

```
PyDataTools/
├── app/                          # 应用主目录
│   ├── __init__.py
│   ├── main.py                   # Streamlit主应用入口
│   └── config.py                 # 应用配置
│
├── modules/                       # 功能模块目录
│   ├── __init__.py
│   └── regression/               # 线性回归模块
│       ├── __init__.py
│       ├── core.py               # 核心回归计算函数
│       ├── data_generator.py    # 数据生成功能
│       ├── plotter.py            # 绘图功能
│       └── web_ui.py             # Web界面组件
│
├── utils/                        # 工具函数目录
│   ├── __init__.py
│   ├── file_handler.py           # 文件处理工具
│   └── visualization.py          # 可视化工具
│
├── data/                         # 数据文件目录
│   ├── samples/                  # 示例数据
│   └── outputs/                  # 输出结果
│
├── static/                       # 静态资源目录
│   └── assets/                  # 图片、样式等
│
├── requirements.txt              # 依赖包列表
└── README.md                     # 项目说明
```

## 安装依赖

```bash
pip install -r requirements.txt
# 或使用 uv
uv pip install -r requirements.txt
```

## 使用方法

### 网页应用（推荐）

启动网页应用：
```bash
streamlit run app/main.py
```

然后在浏览器中打开显示的地址（通常是 http://localhost:8501）

**网页功能：**
- 📤 上传CSV文件
- 📊 自动进行线性回归分析
- 📈 可视化结果展示
- 📥 下载结果图像
- 📋 查看详细数据表格

### 命令行使用

#### 1. 生成测试数据
```bash
python -m modules.regression.data_generator
```

#### 2. 执行回归分析并绘制结果
```bash
python -m modules.regression.plotter
```

## CSV文件格式要求

CSV文件必须包含以下两列：
- `X` - 特征变量（自变量）
- `Y` - 目标变量（因变量）

示例：
```csv
X,Y
1.0,2.5
2.0,4.8
3.0,7.2
```

## 输出结果说明

线性回归分析会输出以下结果：

- **斜率 (Slope)**: 回归系数，表示X每增加1个单位，Y的变化量
- **截距 (Intercept)**: Y轴截距
- **决定系数 (R²)**: 模型拟合度评估（0-1之间，越接近1越好）

## 技术栈

- **Python 3.8+**
- **Streamlit** - Web应用框架
- **Pandas** - 数据处理
- **NumPy** - 数值计算
- **Matplotlib** - 数据可视化
- **Scikit-learn** - 机器学习算法

## 开发计划

- [x] 线性回归分析模块
- [ ] 参数拟合模块
- [ ] 矩阵运算模块
- [ ] 单元测试
- [ ] 文档完善

## 许可证

MIT License
