import pkg10
import pkg20


def main():
    print("Hello from 250726-uv-study-master!")
    print("Now calling pkg10:")
    pkg10.main()

    print("\n" + "="*50)
    print("Now using pkg20 Calculator:")
    # 使用 pkg20 的计算器
    calc = pkg20.Calculator()

    # 进行一些计算
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"20 - 7 = {calc.subtract(20, 7)}")
    print(f"6 * 8 = {calc.multiply(6, 8)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"2 ^ 10 = {calc.power(2, 10)}")

    # 计算平均值
    numbers = [1, 2, 3, 4, 5]
    print(f"Average of {numbers} = {calc.calculate_average(numbers)}")

    # 显示历史记录
    print(f"Calculation history: {calc.get_history()}")


if __name__ == "__main__":
    main()
