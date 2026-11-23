class Plant:
    def __init__(
        self, name: str = "", height: float = 0.0, age: int = 0
    ) -> None:
        self._name: str = name
        if height >= 0:
            self._height: float = float(height)
        else:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        if age >= 0:
            self._age: int = int(age)
        else:
            print(f"{self._name}: Error, age can't be negative")
            self._age = 0

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = float(height)
            print(f"Height updated: {height} cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = int(age)
            print(f"Age updated: {age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 25.0, 30)
    rose.show()
    print("---")
    rose.set_height(-5.0)
    rose.set_age(-10)
    print("---")
    rose.show()
