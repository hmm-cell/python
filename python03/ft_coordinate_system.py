import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        try:
            parts = user_input.split(",")
            if len(parts) != 3:
                print("Invalid syntax")
                continue
            x = float(parts[0])
            y = float(parts[1])
            z = float(parts[2])
            return (x, y, z)
        except ValueError as err:
            print(f"Error on parameter: {err}")


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    coords0 = get_player_pos()
    print(f"Got a first tuple: {coords0}")
    print(f"It includes: X={coords0[0]}, Y={coords0[1]}, Z={coords0[2]}")
    dist_to_center = round(
        math.sqrt(coords0[0] ** 2 + coords0[1] ** 2 + coords0[2] ** 2),
        4,
    )
    print(f"Distance to center: {dist_to_center}")

    print("Get a second set of coordinates")
    coords1 = get_player_pos()
    dist_btwn = round(
        math.sqrt(
            (coords1[0] - coords0[0]) ** 2
            + (coords1[1] - coords0[1]) ** 2
            + (coords1[2] - coords0[2]) ** 2
        ),
        4,
    )
    print(f"Distance between the sets of coordinates: {dist_btwn}")


if __name__ == "__main__":
    main()
