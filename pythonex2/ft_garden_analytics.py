class Plant:
    def __init__(self, name="Unknown plant", height=0.0, age=0):
        self.name = name
        self.height = float(height)
        self.age = age
        
        # Track counts per instance
        self.grow_count = 0
        self.age_count = 0
        self.show_count = 0

    @staticmethod
    def is_more_than_a_year(days):
        """Checks if given days are strictly greater than a year (365 days)."""
        return days > 365

    def stats(self):
        print(f"[statistics for {self.name}]")
        print(f"Stats: {self.grow_count} grow, {self.age_count} age, {self.show_count} show")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def grow_and_bloom(self, height_gain):
        self.grow_count += 1
        self.height += height_gain
        self.is_blooming = True
        print(f"[asking the {self.name.lower()} to grow and bloom]")

    def show(self):
        self.show_count += 1
        print(f"=== Flower")
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)
        self.shade_count = 0

    def produce_shade(self):
        self.shade_count += 1
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {round(self.height, 1)}cm long and {round(self.trunk_diameter, 1)}cm wide.")

    def show(self):
        self.show_count += 1
        print(f"=== Tree")
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def grow_age_and_bloom(self, height_gain, age_gain, seed_count):
        self.grow_count += 1
        self.age_count += 1
        self.height += height_gain
        self.age += age_gain
        self.is_blooming = True
        self.seeds = seed_count
        print(f"[make {self.name.lower()} grow, age and bloom]")

    def show(self):
        self.show_count += 1
        print(f"=== Seed")
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")
        print(f"Seeds: {self.seeds}")


# Base Plant class fallback representation for Anonymous
class AnonymousPlant(Plant):
    def show(self):
        self.show_count += 1
        print(f"=== Anonymous")
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


print("=== Garden statistics ===")

# 1Yearcheck
print("=== Check year-old")
print(f"Is 30 days more than a year? -> {Plant.is_more_than_a_year(30)}")
print(f"Is 400 days more than a year? -> {Plant.is_more_than_a_year(400)}")

# 2Flower
rose = Flower("Rose", 15.0, 10, "red")
rose.show()
rose.stats()

rose.grow_and_bloom(8.0)
rose.show()
rose.stats()

# 3Tree
oak = Tree("Oak", 200.0, 365, 5.0)
oak.show()
oak.stats()
print(f"{oak.shade_count} shade")

oak.produce_shade()
oak.stats()
print(f"{oak.shade_count} shade")

# 4Seed
sunflower = Seed("Sunflower", 80.0, 45, "yellow")
sunflower.show()
sunflower.grow_age_and_bloom(30.0, 20, 42)
rose.show()  # To match the 2 show calls in the stats tracker logic
sunflower.show()
sunflower.stats()

# 5Anonymous
anon = AnonymousPlant()
anon.show()
anon.stats()
