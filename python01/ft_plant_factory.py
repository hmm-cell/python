class Plant:
    def __init__(self, name: str, height: float, age: int):
        """Initialize the plant with its name, height, and age."""
        self.name = name
        self.height = height
        self.age = age

plants = [
    Plant("Rose", 25.0, 30),
    Plant("Oak", 200.0, 365),
    Plant("Cactus", 5.0, 90),
    Plant("Sunflower", 80.0, 45),
    Plant("Fern", 15.0, 120)
]

print("=== Plant Factory Output ===")
for i in range(len(plants)):
    current_plant = plants[i]
    # Format height to one decimal place using round()
    formatted_height = round(current_plant.height, 1)
    print(f"Created: {current_plant.name}: {formatted_height}cm, {current_plant.age} days old")
