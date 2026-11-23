class Plant:
    def __init__(self, name="", height=0.0, age=0):
        self._name = name
        
        if height >= 0:
            self._height = float(height)
        else:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0  # Fallback to default value
            
        if age >= 0:
            self._age = int(age)
        else:
            print(f"{self._name}: Error, age can't be negative")
            self._age = 0  # Fallback to default value

    # Safe Accessors (Getters)
    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    # Controlled Modifiers (Setters)
    def set_height(self, height):
        if height >= 0:
            self._height = float(height)
            print(f"Height updated: {height} cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age):
        if age >= 0:
            self._age = int(age)
            print(f"Age updated: {age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def display_status(self):
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    
    rose = Plant("Rose", 25.0, 30)
    rose.display_status()
    print("---")

    rose.set_height(-5.0)
    rose.set_age(-10)
    print("---")

    rose.display_status()
