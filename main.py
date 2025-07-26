import pkg10
import importlib


def main():
    print("Hello from 250726-uv-study-master!")
    print("Now calling pkg10:")
    pkg10.main()

    print("\n" + "="*50)
    print("Now calling 250726-uv-study-pkg20:")
    # 导入新安装的包
    pkg20_module = importlib.import_module('250726_uv_study_pkg20')
    pkg20_module.main()


if __name__ == "__main__":
    main()
