# UV 使用研究项目

这是一个专门研究 [uv](https://docs.astral.sh/uv/) Python 包管理器的项目，展示了 uv 的各种功能和最佳实践。

## 项目概述

本项目通过实际示例演示了 uv 的核心功能，包括：
- 项目初始化和包创建
- workspace 多包管理
- 依赖管理和解析
- 包安装和卸载
- 开发环境配置

## 项目结构

```
250726-uv-study/
├── pyproject.toml          # 根项目配置，包含 workspace 设置
├── main.py                 # 根目录主入口文件
├── pkg/                    # 包目录
│   ├── pkg1/              # 包1：依赖 pkg2
│   │   ├── pyproject.toml
│   │   ├── src/pkg1/__init__.py
│   │   └── README.md
│   ├── pkg2/              # 包2：依赖 pkg3
│   │   ├── pyproject.toml
│   │   ├── src/pkg2/__init__.py
│   │   └── README.md
│   └── pkg3/              # 包3：基础包
│       ├── pyproject.toml
│       ├── src/pkg3/__init__.py
│       └── README.md
└── ...其他配置文件
```

## 功能演示

### 1. 包依赖链演示
项目展示了复杂的包依赖关系：`pkg1 → pkg2 → pkg3`

```bash
# 运行 pkg1，会依次调用 pkg2 和 pkg3
uv run pkg1
# 输出：
# Hello from pkg1!
# Calling pkg2:
# Hello from pkg2!
# Calling pkg3:
# Hello from pkg3!
```

### 2. 单独运行各个包
```bash
uv run pkg1  # 运行 pkg1
uv run pkg2  # 运行 pkg2  
uv run pkg3  # 运行 pkg3
```

## 核心配置说明

### 1. Workspace 配置
```toml
[tool.uv.workspace]
members = ["pkg/pkg1", "pkg/pkg2", "pkg/pkg3"]
```
- 定义 workspace 成员包
- 共享同一个虚拟环境
- 统一管理依赖版本

### 2. Sources 配置
```toml
[tool.uv.sources]
pkg2 = { workspace = true }
pkg3 = { workspace = true }
```
- 配置 workspace 内部依赖解析
- 允许包之间相互依赖
- 自动处理依赖关系

## UV 命令使用

### 项目初始化
```bash
# 创建应用程序项目
uv init my-app

# 创建打包应用程序
uv init --package my-pkg

# 创建库项目
uv init --lib my-lib

# 创建扩展模块项目（Rust）
uv init --build-backend maturin my-ext
```

### 依赖管理
```bash
# 同步 workspace 依赖
uv sync

# 安装包（可编辑模式）
uv pip install -e pkg/pkg1 -e pkg/pkg2 -e pkg/pkg3

# 卸载包
uv pip uninstall pkg3

# 查看已安装的包
uv pip list
```

### 运行脚本
```bash
# 运行 Python 文件
uv run main.py

# 运行包命令
uv run pkg1
uv run pkg2
uv run pkg3
```

## 开发环境

### 环境要求
- Python >= 3.12
- uv 最新版本

### 快速开始
```bash
# 1. 克隆项目
git clone <repository-url>
cd 250726-uv-study

# 2. 同步依赖
uv sync

# 3. 安装包
uv pip install -e pkg/pkg1 -e pkg/pkg2 -e pkg/pkg3

# 4. 运行演示
uv run pkg1
```

## 研究内容

### 1. 包管理对比
- uv vs pip：性能对比
- uv vs poetry：功能对比
- uv vs pipenv：使用体验对比

### 2. Workspace 功能
- 多包项目管理
- 依赖共享和解析
- 开发便利性

### 3. 依赖解析
- workspace 内部依赖
- 外部依赖管理
- 版本冲突解决

### 4. 构建系统
- 不同构建后端对比
- 扩展模块支持
- 发布流程

## 最佳实践

### 1. 项目结构
- 使用 `src/` 布局
- 清晰的包命名
- 合理的依赖关系

### 2. 依赖管理
- 明确依赖版本
- 避免循环依赖
- 使用 workspace 管理相关包

### 3. 开发流程
- 使用可编辑模式安装
- 定期同步依赖
- 及时更新 lock 文件

## 相关链接

- [UV 官方文档](https://docs.astral.sh/uv/)
- [UV GitHub](https://github.com/astral-sh/uv)
- [Taskfile](https://taskfile.dev) - 项目任务管理
- [Dev Container](https://code.visualstudio.com/docs/devcontainers/containers) - 开发环境

## 作者

- GitHub: [lwmacct](https://github.com/lwmacct)
- 语雀: [Dev Containers 使用指南](https://www.yuque.com/lwmacct/vscode/dev-containers)

## 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。
