class Plant:
    def __init__(
        self,
        name: str = "",
        height: float = 0.0,
        age: int = 0,
        growth_rate: float = 0.0,
    ) -> None:
        self.name: str = name
        self.height: float = float(height)
        self.age: int = age
        self.growth_rate: float = float(growth_rate)
        self.total_growth: float = 0.0

    def grow(self) -> None:
        self.height += self.growth_rate
        self.total_growth += self.growth_rate

    def age_up(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.age} days old"
        )


def main() -> None:
    rose = Plant("Rose", 25.0, 30, 0.8)

    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age_up()
        rose.show()

    print(f"Growth this week: {round(rose.total_growth, 1)}cm")


if __name__ == "__main__":
    main()
