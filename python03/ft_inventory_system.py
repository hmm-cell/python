import sys


def main() -> None:
    inventory: dict[str, int] = {}
    arguments = sys.argv[1:]

    print("=== Inventory System Analysis ===")

    for argument in arguments:
        if ":" not in argument:
            print(f"Error - invalid parameter '{argument}'")
            continue

        parts = argument.split(":", 1)
        item = parts[0]

        if item in inventory.keys():
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            amount = int(parts[1])
            inventory.update({item: amount})
        except ValueError as err:
            print(f"Quantity error for '{item}': {err}")

    print(f"Got inventory: {inventory}")

    items_list = list(inventory.keys())
    print(f"Item list: {items_list}")

    total_values = sum(inventory.values())
    total_keys = len(inventory.keys())
    print(f"Total quantity of the {total_keys} items: {total_values}")

    if total_values > 0:
        for item, quantity in inventory.items():
            percentage = round((quantity / total_values) * 100, 1)
            print(f"Item {item} represents {percentage}%")

        items_items = list(inventory.items())
        most_abundant = items_items[0][0]
        max_value = items_items[0][1]
        for item, quantity in inventory.items():
            if quantity > max_value:
                max_value = quantity
                most_abundant = item
        print(f"Item most abundant: {most_abundant} with quantity {max_value}")

        least_abundant = items_items[0][0]
        min_value = items_items[0][1]
        for item, quantity in inventory.items():
            if quantity < min_value:
                min_value = quantity
                least_abundant = item
        print(f"Item least abundant: {least_abundant} with quantity {min_value}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
