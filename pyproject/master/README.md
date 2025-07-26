# Master Application

基于 uv 的 Python 包管理最佳实践示例。

## 项目结构

```
master/
├── master/           # 主应用包
│   ├── __init__.py
│   └── main.py
├── main.py          # 应用入口点
├── pyproject.toml   # 项目配置
├── uv.lock         # 依赖锁定文件
├── scripts/        # 管理脚本
│   └── manage-deps.sh
└── README.md       # 本文档
```

## 依赖关系

```
master
└── pkg3 (Git SSH)
    ├── pkg1 (Git SSH)
    └── pkg2 (Git SSH)
```

## 快速开始

### 1. 安装依赖

```bash
# 同步环境（推荐）
uv sync

# 或者使用脚本
./scripts/manage-deps.sh sync
```

### 2. 运行应用

```bash
# 正常运行
uv run python main.py

# 使用锁定版本（生产环境推荐）
uv run --locked python main.py

# 使用冻结模式
uv run --frozen python main.py
```

## 依赖管理

### 使用管理脚本

```bash
# 检查 lock 文件状态
./scripts/manage-deps.sh check

# 预览 lock 文件更改
./scripts/manage-deps.sh preview

# 升级所有包
./scripts/manage-deps.sh upgrade

# 升级特定包
./scripts/manage-deps.sh upgrade-pkg pkg1

# 刷新缓存
./scripts/manage-deps.sh refresh

# 同步环境
./scripts/manage-deps.sh sync

# 运行测试
./scripts/manage-deps.sh test

# 执行完整流程
./scripts/manage-deps.sh all
```

### 手动管理

```bash
# 检查 lock 文件状态
uv lock --check

# 预览更改
uv lock --dry-run

# 升级所有包
uv lock --upgrade

# 升级特定包
uv lock --upgrade-package pkg1

# 刷新缓存
uv lock --refresh

# 同步环境
uv sync
```

## 最佳实践

### 开发环境

```bash
# 正常开发流程
uv sync
uv run python main.py

# 强制刷新特定包
uv sync --refresh-package pkg1

# 强制重新安装
uv sync --reinstall
```

### 生产环境

```bash
# 使用锁定版本，确保一致性
uv run --locked python main.py

# 或者使用冻结模式
uv run --frozen python main.py
```

### 调试依赖问题

```bash
# 强制重新验证所有缓存
uv sync --refresh

# 强制重新安装所有包
uv sync --reinstall

# 清理缓存并重新安装
rm -rf .venv
rm -rf /root/.cache/uv
uv sync
```

## 环境变量

- `UV_LOCKED=1`: 等同于 `--locked` 选项
- `UV_FROZEN=1`: 等同于 `--frozen` 选项
- `UV_NO_CACHE=1`: 避免使用缓存
- `UV_REFRESH=1`: 强制刷新缓存

## 故障排除

### 包导入错误

如果遇到 `ModuleNotFoundError`：

1. 检查 lock 文件状态：
   ```bash
   uv lock --check
   ```

2. 刷新缓存：
   ```bash
   uv sync --refresh
   ```

3. 重新安装：
   ```bash
   uv sync --reinstall
   ```

### 版本不一致

如果包版本不是最新的：

1. 升级所有包：
   ```bash
   uv lock --upgrade
   ```

2. 同步环境：
   ```bash
   uv sync
   ```

### 缓存问题

如果怀疑缓存有问题：

1. 清理缓存：
   ```bash
   rm -rf /root/.cache/uv
   ```

2. 重新同步：
   ```bash
   uv sync
   ```

## 参考

- [uv 官方文档](https://docs.astral.sh/uv/)
- [uv lock 命令](https://docs.astral.sh/uv/commands/lock/)
- [uv sync 命令](https://docs.astral.sh/uv/commands/sync/)
- [uv run 命令](https://docs.astral.sh/uv/commands/run/)
