# 🧪 SauceDemo 自动化测试项目

本项目基于 [https://www.saucedemo.com](https://www.saucedemo.com) 电商演示网站，实现了完整的 UI 自动化测试流程，涵盖登录、加购物车、结账流程，采用 POM 模型开发，集成 Allure 报告和失败截图。

## 🚀 功能特点

- ✅ 多用户登录验证（包括异常用户、性能测试用户等）
- ✅ 商品添加至购物车
- ✅ 购物车跳转与结账流程
- ✅ 异常用户跳过结算逻辑
- ✅ POM（Page Object Model）封装页面逻辑
- ✅ Pytest 数据驱动测试（基于 YAML）
- ✅ Allure 报告集成，生成图形化测试报告
- ✅ 测试失败截图自动保存

## 🛠 技术栈

- Python 3.13
- Selenium 4
- Pytest
- YAML
- Allure-Pytest
- Page Object Model（POM）

## 📁 项目结构说明
```
pytest-saucedemo/
│
├── data.yaml # 测试数据文件（登录+结账）
├── pyproject.toml # 项目依赖管理
├── README.md # 项目说明
│
├── src/
│ ├── config.yaml # 全局配置文件（网站地址等）
│ ├── conftest.py # Pytest 配置和 driver fixture
│ ├── pages/ # 页面对象封装（POM）
│ ├── tests/ # 测试用例
│ └── utils/ # 工具类（配置、日志、数据读取）
│
├── test_failed_*.png # 测试失败截图
├── test.log # 测试日志文件



## 📸 测试报告展示

生成 Allure 报告：

# 运行测试并生成 Allure 报告数据
pytest src/tests --alluredir=./allure-results

# 启动本地服务器查看图形报告
allure serve ./allure-results

## 🧪 快速开始

# 安装依赖（建议使用虚拟环境）
pip install -r requirements.txt

# 运行测试
pytest src/tests -s

# 查看失败截图或 test.log 日志以排查问题
