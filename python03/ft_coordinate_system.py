import math

def get_player_pos():
    cords = ()
    print(f"=== Game Coordinate System ===")
    print()
    
    while True:
        user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            x, y, z = [float(i) for i in user_input.split(',')]
            return (x, y, z)
            
        except ValueError:
            print(f"Invalid syntax")

coords0 = get_player_pos()
print(f"Got a first tuple: ({coords0})")
print(f"It includes: X={coords0[0]}, Y={coords0[1]}, Z={coords0[2]}")
dist_to_center = math.sqrt(coords0[0]**2 + coords0[1]**2 + coords0[2]**2)
print(f"Distance to center: {dist_to_center}")

print(f"Get a second set of coordinates")
coords1 = get_player_pos()
print(f"Got a first tuple: ({coords1})")
print(f"It includes: X={coords1[0]}, Y={coords1[1]}, Z={coords1[2]}")
dist_to_center = math.sqrt(coords1[0]**2 + coords1[1]**2 + coords1[2]**2)
print(f"Distance to center: {dist_to_center}")

dist_btwn = math.sqrt((c1[0] - c0[0])**2 + (c1[1] - c0[1])**2 + (c1[2] - c0[2])**2)
print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}")
