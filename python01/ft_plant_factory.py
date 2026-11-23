class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def show(self) -> None:
        formatted_height = round(self.height, 1)
        print(
            f"Created: {self.name}: {formatted_height}cm, "
            f"{self.age} days old"
        )


def main() -> None:
    plants: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.show()


if __name__ == "__main__":
    main()
