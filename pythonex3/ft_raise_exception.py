def input_temperature(temp_str):
    temp = int(temp_str)
    if 0 <= temp <= 40:
        return temp
    else:
        if temp > 40:
            raise ValueError(f"{temp_str}"°C is too hot for plants (max 40°C)")
        else:
            raise ValueError(f"{temp_str}"°C is too cold for plants (min 0°C)")

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

    print("Input data is '100'")
    try:
        valid_res = input_temperature("100")
        print(f"Input data is '{}'")
    print("All tests completed - program didn't crash!")
                             

test_temperature()
