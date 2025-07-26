from demo1.main import get_message, calculate_sum


def main():
    print("Hello from demo2!")

    # 使用 demo1 的功能
    message = get_message()
    print(f"从 demo1 获取的消息: {message}")

    result = calculate_sum(10, 20)
    print(f"使用 demo1 计算 10 + 20 = {result}")


if __name__ == "__main__":
    main()
