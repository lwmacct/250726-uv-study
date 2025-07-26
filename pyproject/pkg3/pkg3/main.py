from pkg1.main import get_message, calculate_sum
from pkg2.main import process_data, format_output


def main():
    print("Hello from pkg3!")


def run_business_logic():
    """运行业务逻辑，使用 pkg1 和 pkg2 的功能"""
    # 使用 pkg1 的功能
    message = get_message()
    result = calculate_sum(10, 20)

    # 使用 pkg2 的功能
    processed = process_data(f"{message} - Sum: {result}")
    formatted = format_output(processed)

    return formatted


def combine_functions():
    """组合 pkg1 和 pkg2 的功能"""
    return {
        "pkg1_message": get_message(),
        "pkg1_sum": calculate_sum(5, 15),
        "pkg2_processed": process_data("test data"),
        "pkg2_formatted": format_output("test result")
    }


if __name__ == "__main__":
    main()
