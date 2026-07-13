def garden_operations(operation_number):
    if operation_number == 0:
        int("abc")
    #ValueError because abc isnt a number
    elif operation_number == 1:
        10 / 0
    #ZeroDivisionError because you cannot devide by 0
    elif operation_number == 2:
        open("file.txt", "r")
    #FileNotFoundError becuase this file does not exist
    elif operation_number == 3:
        5 + "plants"
    #TypeError because you cannot add two different data types
    else:
        return

def test_error_type():

    for num in range(4):
    try:
        garden_operations(num)
    except ValueError:
        
        
    
    
        
