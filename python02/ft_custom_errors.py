class GardenError(Exception):
    """Basic error for all garden problems."""

    def __init__(self, message: str = "A garden error occurred") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Error specific to plants."""

    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Error specific to watering."""

    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test_plant_err() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water_err() -> None:
    raise WaterError("Not enough water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")

    try:
        test_plant_err()
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print()

    try:
        test_water_err()
    except WaterError as err:
        print(f"Caught WaterError: {err}")
        print()

    print("Testing catching all garden errors...")

    try:
        test_plant_err()
    except GardenError as err:
        print(f"Caught GardenError: {err}")

    try:
        test_water_err()
    except GardenError as err:
        print(f"Caught GardenError: {err}")

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
