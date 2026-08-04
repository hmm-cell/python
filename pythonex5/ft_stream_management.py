import sys
import typing

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <file>")
    sys.exit(1)

filename = sys.argv[1]

print("=== Cyber Archives Recovery & Preservation ===")
print(f"Accessing file '{filename}'")

try:
    file: typing.IO = open(filename, 'r')
    content = file.read()
    file.close()
    
    print("---")
    print(content, end="" if content.endswith("\n") else "\n")
    print("---")
    print(f"File '{filename}' closed.")
    
except Exception as err:
    print(f"[STDERR] Error opening file '{filename}': {err}", file=sys.stderr)
    sys.exit(1)

modified_content = ""
if content:
    content_clean = content[:-1] if content.endswith('\n') else content
    lines = content_clean.split('\n')
    
    for line in lines:
        modified_content += line + "#\n"
        
    if not content.endswith('\n'):
        modified_content = modified_content[:-1]

print("Transform data:")
print("---")
print(modified_content, end="" if modified_content.endswith("\n") else "\n")
print("---")

new_filename = input("Enter new file name (or empty): ")

if new_filename == "":
    new_filename = filename

print(f"Saving data to '{new_filename}'")

try:
    file = open(new_filename, 'w')
    file.write(modified_content)
    file.close()
    print(f"Data saved in file '{new_filename}'.")
    
except Exception as err:
    print(f"[STDERR] Error saving file '{new_filename}': {err}, file=sys.stderr")
    sys.exit(1)
