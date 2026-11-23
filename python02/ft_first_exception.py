def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()

    print("Input data is '25'")
    try:
        temp = input_temperature("25")
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")

    print()
    print("Input data is 'abc'")
    try:
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")

    print()
    print("All tests completed program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
