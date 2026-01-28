# Streamlit Cloud 部署指南

## 前置准备

1. ✅ GitHub 账号已注册
2. ✅ 项目代码已准备好
3. ✅ requirements.txt 已配置

## 部署步骤

### 第一步：在 GitHub 上创建仓库

1. 登录 GitHub (https://github.com)
2. 点击右上角的 "+" 号，选择 "New repository"
3. 填写仓库信息：
   - **Repository name**: `PyDataToolsClairDong` (或你喜欢的名字)
   - **Description**: Python数据处理工具 - 线性回归、参数拟合、矩阵运算等
   - **Visibility**: 
     - Public（公开，免费使用 Streamlit Cloud）
     - Private（私有，需要 Streamlit Cloud Team 计划）
   - **不要**勾选 "Initialize this repository with a README"（因为我们已经有了）
4. 点击 "Create repository"

### 第二步：将代码推送到 GitHub

在项目目录执行以下命令：

```bash
# 初始化 git 仓库
git init

# 添加所有文件
git add .

# 提交代码
git commit -m "Initial commit: PyDataTools - Python数据处理工具"

# 添加远程仓库（替换 YOUR_USERNAME 和 YOUR_REPO_NAME）
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

### 第三步：在 Streamlit Cloud 上部署

1. 访问 https://share.streamlit.io/
2. 点击 "Sign in" 使用 GitHub 账号登录
3. 授权 Streamlit Cloud 访问你的 GitHub 仓库
4. 点击 "New app" 创建新应用
5. 填写部署信息：
   - **Repository**: 选择你刚创建的仓库
   - **Branch**: `main` (或 `master`)
   - **Main file path**: `app/main.py` ⚠️ **重要：这是应用入口文件**
   - **App URL**: 会自动生成（如：`https://pydatatools.streamlit.app`）
6. 点击 "Deploy!"

### 第四步：等待部署完成

- 首次部署可能需要 2-5 分钟
- 部署过程中会显示日志
- 部署成功后会自动打开应用

## 后续更新

每次更新代码后，只需：

```bash
git add .
git commit -m "更新说明"
git push
```

Streamlit Cloud 会自动检测到更新并重新部署（通常需要 1-2 分钟）。

## 注意事项

1. **Main file path** 必须填写 `app/main.py`
2. 确保 `requirements.txt` 包含所有依赖
3. 如果使用私有仓库，需要 Streamlit Cloud Team 计划
4. 免费版有资源限制，但足够运行此应用

## 故障排查

如果部署失败：
1. 检查 `requirements.txt` 是否正确
2. 检查 `app/main.py` 路径是否正确
3. 查看部署日志中的错误信息
4. 确保所有依赖包版本兼容
