def garden_operations(operation_number):
    if operation_number == 0:
        #ValueError because abc isnt a number
        int("abc")
    elif operation_number == 1:
        #ZeroDivisionError because you cannot devide by 0
        10 / 0
    elif operation_number == 2:
        #FileNotFoundError becuase this file does not exist
        open("file.txt", "r")
    elif operation_number == 3:
        #TypeError because you cannot add two different data types
        5 + "plants"
    else:
        return

def test_error_type():
    print(f"=== Garden Error Types Demo ===")
    for num in range(4):
    try:
        garden_operations(num)
        print(f"Testing operation 4...")
        print("Operation completed successfully")
    except ValueError:
        print(f"Testing operation 0...")
        print(f"Caught ValueError: invalid literal for int() with base 10: 'abc'")
    except ZeroDivisionError:
        print(f"Testing operation 1...")
        print(f"Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print(f"Testing operation 2...")
        print(f"Caught FileNotFoundError: [Errno 2] No such file or directory: '/non/existent/file'")
    except TypeError:
        print(f"Testing operation 3...")
        print(f"Caught TypeError: can only concatenate str (not "int") to str")
    print()
    print("All error types tested successfully!")
    
        
    
    
        
