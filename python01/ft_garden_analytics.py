class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0
            self._shade_calls: int = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self, name: str, include_shade: bool = False) -> None:
            print(f"[statistics for {name}]")
            line = (
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )
            if include_shade:
                line += f", {self._shade_calls} shade"
            print(line)

    def __init__(
        self,
        name: str = "Unknown plant",
        height: float = 0.0,
        age: int = 0,
    ) -> None:
        self._name: str = name
        self._height: float = float(height)
        self._age: int = age
        self._stats: Plant._Stats = Plant._Stats()

    @property
    def name(self) -> str:
        return self._name

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls(name="Unknown plant", height=0.0, age=0)

    @staticmethod
    def is_more_than_a_year(days: int) -> bool:
        return days > 365

    def grow(self, amount: float = 1.0) -> None:
        self._height += amount
        self._stats.record_grow()

    def age_up(self, days: int = 1) -> None:
        self._age += days
        self._stats.record_age()

    def show(self) -> None:
        self._stats.record_show()
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._is_blooming: bool = False

    def grow_and_bloom(self, height_gain: float) -> None:
        print(f"[asking the {self._name.lower()} to grow and bloom]")
        self.grow(height_gain)
        self._is_blooming = True

    def show(self) -> None:
        self._stats.record_show()
        print("=== Flower")
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")
        print(f"Color: {self._color}")
        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: float = float(trunk_diameter)

    def produce_shade(self) -> None:
        print(f"[asking the {self._name.lower()} to produce shade]")
        self._stats.record_shade()
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{round(self._trunk_diameter, 1)}cm wide."
        )

    def show(self) -> None:
        self._stats.record_show()
        print("=== Tree")
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self._seeds: int = 0

    def grow_age_and_bloom(
        self, height_gain: float, age_gain: int, seed_count: int
    ) -> None:
        print(f"[make {self._name.lower()} grow, age and bloom]")
        self.grow(height_gain)
        self.age_up(age_gain)
        self._is_blooming = True
        self._seeds = seed_count

    def show(self) -> None:
        self._stats.record_show()
        print("=== Seed")
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")
        print(f"Color: {self._color}")
        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")
        print(f"Seeds: {self._seeds}")


def display_plant_statistics(plant: Plant) -> None:
    plant._stats.display(
        plant.name, include_shade=isinstance(plant, Tree)
    )


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_more_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_more_than_a_year(400)}")

    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_statistics(rose)

    rose.grow_and_bloom(8.0)
    rose.show()
    display_plant_statistics(rose)

    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_statistics(oak)

    oak.produce_shade()
    display_plant_statistics(oak)

    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    sunflower.grow_age_and_bloom(30.0, 20, 42)
    sunflower.show()
    display_plant_statistics(sunflower)

    anon = Plant.create_anonymous()
    print("=== Anonymous")
    anon.show()
    display_plant_statistics(anon)


if __name__ == "__main__":
    main()
