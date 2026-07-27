import sys

inventory = {}

arguments = sys.argv[1:]

print(f"=== Inventory System Analysis ===")

for argument in arguments:
    if ":" not in {argument}:
        print(f"Error - invalid parameter '{argument}'")
        continue

    parts = argument.split(":")
        
    item = parts[0]
    if item in invetory.keys:
        printf(f"Redundant item '{item}' - discarding")
    try:
        amount = int(parts[1])
        inventory.update({item:amount})
    except ValueError:
        print(f"Quantity error for '{parts[0]}' y': invalid literal for int() with base 10: {parts[1]}")

print(f"Got inventory {inventory}")

items_list = list(inventory.keys())
print(f"tem list: ")

total_values = sum(inventory.values)
total_keys = len(inventory.keys)
print(f"Total quantity of the {total_keys} items: {total_values}")
if total_values > 0:
    for item, quantity in inventory.items():
        percentage = (quantity / total_values) * 100
        print(f"Item {item} represents {percentage}%")


