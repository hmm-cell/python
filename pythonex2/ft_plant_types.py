class Plant:
    def __init__(self, name="", height=0, age=0):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self):
        self.is_blooming = True
        print(f"[asking the {self.name.lower()} to bloom]")
        

    def show(self):
        print(f"=== Flower")
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old.")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

class Tree(Plant):
    def __init__(self, name, height, age,  trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_length = 0.0
        self.shade_width = 0.0

    def produce_shade(self):
        self.shade_length = round(self.height, 1)
        self.shade_width = round(self.trunk_diameter, 1)
        print(f"Tree {self.name} now produces a shade of {self.shade_length} cm long and {self.shade_width} cm wide.")

    def show(self):
        print(f"=== Tree")
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old.")
        print(f"{round(self.trunk_diameter, 1)}cm")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest):
        super().__init__(name, height, age)
        self.harvest = harvest
        self.nutrition = 0

    def grow(self):
        print(f"[make {self.name.lower()} grow and age for 20 days]")
        self.nutrition = self.nutrition + 20
        self.age = self.age + 20
        self.height = self.height + 42.0
        
    def show(self):
        print(f"=== Vegetable")
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old.")
        print(f"Harvest season: {self.harvest}")
        print(f"Nutritional value: {self.nutrition}")

if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    
    rose = Flower(name="Rose", height=15.0, age=10, color="red")
    rose.show()
    rose.bloom()
    rose.show()
    
    oak = Tree(name="Oak", height=200.0, age=365, trunk_diameter=5.0)
    oak.show()
    oak.produce_shade()
    
    tomato = Vegetable(name="Tomato", height=5.0, age=10, harvest="April")
    tomato.show()
    tomato.grow()
    tomato.show()
