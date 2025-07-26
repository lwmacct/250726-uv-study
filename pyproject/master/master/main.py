from pkg3.main import run_business_logic, combine_functions


def main():
    print("=== Master Application ===")

    # 使用 pkg3 的业务逻辑
    print("\n1. 运行业务逻辑:")
    result = run_business_logic()
    print(f"   结果: {result}")

    # 使用 pkg3 的组合功能
    print("\n2. 组合功能:")
    combined = combine_functions()
    for key, value in combined.items():
        print(f"   {key}: {value}")

    print("\n=== 应用完成 ===")


if __name__ == "__main__":
    main()
