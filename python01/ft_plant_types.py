class Plant:
    def __init__(self, name: str = "", height: float = 0.0, age: int = 0) -> None:
        self.name: str = name
        self.height: float = float(height)
        self.age: int = age

    def grow(self, amount: float = 1.0) -> None:
        self.height += amount

    def age_up(self, days: int = 1) -> None:
        self.age += days

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.is_blooming: bool = False

    def bloom(self) -> None:
        self.is_blooming = True
        print(f"[asking the {self.name.lower()} to bloom]")

    def show(self) -> None:
        print("=== Flower")
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = float(trunk_diameter)

    def produce_shade(self) -> None:
        length = round(self.height, 1)
        width = round(self.trunk_diameter, 1)
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of "
            f"{length}cm long and {width}cm wide."
        )

    def show(self) -> None:
        print("=== Tree")
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def grow(self, amount: float = 42.0) -> None:
        super().grow(amount)
        self.nutritional_value += 10

    def age_up(self, days: int = 20) -> None:
        super().age_up(days)
        self.nutritional_value += 10

    def show(self) -> None:
        print("=== Vegetable")
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()

    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()

    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42.0)
    tomato.age_up(20)
    tomato.show()


if __name__ == "__main__":
    main()
