Class GardenError(Exception):
    #basic error for all garden problems
    def __init__(self, message = "A garden error occured"):
        super().__init__(message)

Class PlantError(GardenError):
    #error specific to plants
    def __init__(self, message = "Unknown plant error"):
        super().__init__(message)

Class WaterError(GardenError):
    def __init__(self, message = "Unknown plant error"):
        super().__init__(message)

def test_plant_err(PlantError):
    raise PlantError = "Caught PlantError: The tomato plant is wilting!"

def test_water_err(WaterError):
    raise WaterError = "Caught WaterError: Not enough water in the tank!"

def main():
    print(f"=== Custom Garden Errors Demo ===")
    print()
    print(f"Testing PlantError...")
    
    try:
        test_plant_err()
    except PlantError as err:
        print(f"Caught PlantError: The tomato plant is wilting!")
        print()
    try:
        test_water_err()
    except WaterError as err:
        print(f"Caught WaterError: Not enough water in the tank!")
        print()
    print(f"Testing catching all garden errors...")

     try:
        test_plant_err()
    except GardenError as err:
        print(f"Caught GardenError: The tomato plant is wilting!")

    try:
        test_water_err()
    except GardenError as err:
        print(f"Caught GardenError: Not enough water in the tank!")

    print()
    print(f"All custom error types work correctly!")
    
if __name__ == "__main__":
    main()
