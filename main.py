import pkg10
import py_uv_study_pkg20_250726


def main():
    print("Hello from 250726-uv-study-master!")
    print("Now calling pkg10:")
    pkg10.main()

    print("\n" + "="*50)
    print("Now calling py-uv-study-pkg20-250726:")
    # 直接调用包的 main 函数
    py_uv_study_pkg20_250726.main()


if __name__ == "__main__":
    main()
