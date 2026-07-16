import sys

print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
print(f"Arguments recieved: {len(sys.argv) - 1}")

ctr = 1

for arg in sys.argv[1:]:
    print(f"Argument {ctr}: {arg}")
    ctr += 1;

print(f"Total arguments: {len(sys.argv)}")
