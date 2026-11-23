class GardenError(Exception):
    def __init__(self, message="A garden error occurred"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name):
    # O método capitalize() transforma a primeira letra em maiúscula e o resto em minúscula.
    # Se a string original já for igual ao seu capitalize(), significa que ela está capitalizada.
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants_list):
    print("Opening watering system")
    
    try:
        for plant in plants_list:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return  # O return força a saída imediata da função, mas o 'finally' corre ANTES de sair!
    finally:
        print("Closing watering system")


def main():
    print("=== Garden Watering System ===")
    
    # Teste 1: Todas as plantas começam com letra maiúscula (Válidas)
    print("Testing valid plants...")
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(valid_plants)
    
    # Teste 2: A planta 'lettuce' está em minúsculas (Inválida)
    print("Testing invalid plants...")
    invalid_plants = ["Tomato", "lettuce", "Carrots"]
    test_watering_system(invalid_plants)
    
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
