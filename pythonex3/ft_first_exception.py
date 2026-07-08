def input_temperature(temp_str):
    return int(temp_str)

def test_temperature():
    print("Input data is '25'")
    try:
        valid_res = input_temperature("25")
        print(f"Input data is '{valid_res}'")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    print("Input data is 'abc'")
    try:
        valid_res = input_temperature("abc")
        print(f"Input data is '{valid_res}'")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    print("All tests completed - program didn't crash!")

test_temperature()
