class Plant:
    def __init__(self, name="", height=0, age=0):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"Plant Name: {self.name}")
        print(f"Height: {self.height} cm")
        print(f"Age: {self.age} days")
        print("-" * 25)

plant1 = Plant()
plant1.name = "Fern"
plant1.height = 30
plant1.age = 45

plant2 = Plant()
plant2.name = "Cactus"
plant2.height = 15
plant2.age = 120

plant3 = Plant()
plant3.name = "Orchid"
plant3.height = 40
plant3.age = 60

print("--- Plant Information ---\n")
plant1.show()
plant2.show()
plant3.show()
