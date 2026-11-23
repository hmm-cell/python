def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if 0 <= temp <= 40:
        return temp
    if temp > 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
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
    print("Input data is '100'")
    try:
        temp = input_temperature("100")
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")

    print()
    print("Input data is '-50'")
    try:
        temp = input_temperature("-50")
        print(f"Temperature is now {temp}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")

    print()
    print("All tests completed program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
