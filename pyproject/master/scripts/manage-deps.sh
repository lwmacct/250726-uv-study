#!/bin/bash
# shellcheck disable=all

# 改进的依赖管理脚本 - 基于 uv 官方文档最佳实践

__script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
__project_root="$(dirname "$__script_dir")"

echo "=== UV 依赖管理脚本 ==="
echo "项目根目录: $__project_root"
echo

# 函数：检查 lock 文件状态
__check_lock_status() {
  echo "🔍 检查 lock 文件状态..."
  cd "$__project_root" || exit 1

  if uv lock --check; then
    echo "✅ Lock 文件是最新的"
  else
    echo "⚠️  Lock 文件需要更新"
  fi
  echo
}

# 函数：预览 lock 文件更改
__preview_changes() {
  echo "👀 预览 lock 文件更改..."
  cd "$__project_root" || exit 1

  if uv lock --dry-run; then
    echo "✅ 没有检测到 lock 文件更改"
  else
    echo "📝 检测到 lock 文件更改"
  fi
  echo
}

# 函数：升级所有包
__upgrade_all() {
  echo "⬆️  升级所有包..."
  cd "$__project_root" || exit 1

  uv lock --upgrade
  echo "✅ 所有包已升级"
  echo
}

# 函数：升级特定包
__upgrade_package() {
  local _package_name="$1"
  if [[ -z "$_package_name" ]]; then
    echo "❌ 请指定包名"
    return 1
  fi

  echo "⬆️  升级包: $_package_name"
  cd "$__project_root" || exit 1

  uv lock --upgrade-package "$_package_name"
  echo "✅ 包 $_package_name 已升级"
  echo
}

# 函数：刷新缓存
__refresh_cache() {
  echo "🔄 刷新缓存..."
  cd "$__project_root" || exit 1

  uv lock --refresh
  echo "✅ 缓存已刷新"
  echo
}

# 函数：同步环境
__sync_environment() {
  echo "🔄 同步环境..."
  cd "$__project_root" || exit 1

  uv sync
  echo "✅ 环境已同步"
  echo
}

# 函数：运行测试
__run_tests() {
  echo "🧪 运行测试..."
  cd "$__project_root" || exit 1

  echo "测试导入 pkg1..."
  uv run python -c "import pkg1; print('✅ pkg1 导入成功')"

  echo "测试导入 pkg2..."
  uv run python -c "import pkg2; print('✅ pkg2 导入成功')"

  echo "测试导入 pkg3..."
  uv run python -c "import pkg3; print('✅ pkg3 导入成功')"

  echo "测试主应用..."
  uv run python main.py
  echo "✅ 所有测试通过"
  echo
}

# 函数：显示帮助
__show_help() {
  echo "用法: $0 [命令]"
  echo
  echo "命令:"
  echo "  check             检查 lock 文件状态"
  echo "  preview           预览 lock 文件更改"
  echo "  upgrade           升级所有包"
  echo "  upgrade-pkg <包名> 升级特定包"
  echo "  refresh           刷新缓存"
  echo "  sync              同步环境"
  echo "  test              运行测试"
  echo "  all               执行完整流程 (check -> upgrade -> sync -> test)"
  echo "  help              显示此帮助"
  echo
  echo "示例:"
  echo "  $0 check"
  echo "  $0 upgrade-pkg pkg1"
  echo "  $0 all"
}

# 主函数
__main() {
  case "${1:-help}" in
  "check")
    __check_lock_status
    ;;
  "preview")
    __preview_changes
    ;;
  "upgrade")
    __upgrade_all
    ;;
  "upgrade-pkg")
    __upgrade_package "$2"
    ;;
  "refresh")
    __refresh_cache
    ;;
  "sync")
    __sync_environment
    ;;
  "test")
    __run_tests
    ;;
  "all")
    echo "🚀 执行完整流程..."
    __check_lock_status
    __upgrade_all
    __sync_environment
    __run_tests
    ;;
  "help" | *)
    __show_help
    ;;
  esac
}

# 执行主函数
__main "$@"
