import pkg10
import importlib


def main():
    print("Hello from 250726-uv-study-master!")
    print("Now calling pkg10:")
    pkg10.main()

    print("\n" + "="*50)
    print("Now calling py-uv-study-pkg20-250726:")
    # 导入新安装的包
    pkg20_module = importlib.import_module('py_uv_study_pkg20_250726')
    pkg20_module.main()


if __name__ == "__main__":
    main()
