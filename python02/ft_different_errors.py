def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        5 + "plants"
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for num in range(5):
        print(f"Testing operation {num}...")
        try:
            garden_operations(num)
            print("Operation completed successfully")
        except ValueError as err:
            print(f"Caught ValueError: {err}")
        except ZeroDivisionError as err:
            print(f"Caught ZeroDivisionError: {err}")
        except FileNotFoundError as err:
            print(f"Caught FileNotFoundError: {err}")
        except TypeError as err:
            print(f"Caught TypeError: {err}")

    print()
    print("Testing catching multiple errors together...")
    for num in (0, 1, 4):
        try:
            garden_operations(num)
            print(f"Operation {num}: completed successfully")
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as err:
            print(f"Operation {num}: caught error -> {err}")

    print()
    print("All error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
