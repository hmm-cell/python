class GardenError(Exception):
    def __init__(self, message: str = "A garden error occurred") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants_list:
            water_plant(plant)
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(valid_plants)
    print()
    print("Testing invalid plants...")
    invalid_plants = ["Tomato", "lettuce", "Carrots"]
    test_watering_system(invalid_plants)
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
