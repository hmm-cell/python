import sys

print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
if len(sys.argv) > 1:
    print(f"Arguments received: {len(sys.argv) - 1}")
else:
    print(f"No arguments provided!")
ctr = 1

for arg in sys.argv[1:]:
    print(f"Argument {ctr}: {arg}")
    ctr += 1

print(f"Total arguments: {len(sys.argv)}")
