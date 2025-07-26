#!/usr/bin/env python3

import importlib.util


def test_pkg20():
    """测试 250726-uv-study-pkg20 包"""
    try:
        # 动态导入包
        pkg_path = ('.venv/lib/python3.12/site-packages/'
                    '250726_uv_study_pkg20/__init__.py')
        spec = importlib.util.spec_from_file_location('pkg20', pkg_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        print("✅ 250726-uv-study-pkg20 包导入成功")
        print("📦 调用包的 main 函数:")
        module.main()

    except Exception as e:
        print(f"❌ 导入失败: {e}")


if __name__ == "__main__":
    test_pkg20()
