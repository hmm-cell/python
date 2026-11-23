class Plant:
    def __init__(self, name="", height=0, age=0, growth_rate = 0.0):
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate
        self.total_growth = 0.0
      
      def grow_in_day(self):
        self.height += self.growth_rate
        self.age += 1
        self.total_rate += self.growth_rate

    def display_rose_stats(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

rose = Plant()
rose.name = "Rose"
rose.height = 25
rose.age = 30
rose.growth_rate = 0.8

print("=== Garden Plant Growth ===")
rose.display_status()
for day in range(1, 8):
    print(f"=== Day {day} ===")
    rose.grow_in_day()
    rose.display_rose_stats()

print(f"Growth this week: {rose.total_growth:.1f}cm")
