import sys
import typing

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <file>")
    sys.exit(1)

filename = sys.argv[1]
print(f"=== Cyber Archives Recovery ===")
print(f"Accessing file'{filename}'")

try:
    file: typing.IO = open(filename, 'r')
    content = file.read()
    print(f"---\n")
    print(f"{content}")
    print(f"---\n")
    print(f"File '{filename}' closed.")
    file.close()
except Exception as err:
    print(f"Error opening file '{nome_ficheiro}': {err}")
    sys.exit(1)
