def secure_archive(filename: str, action: str = "r", content_w: str = "") -> tuple:
    try:
        if action = "r"
            with open(filename, "r") as file
                return (True, file.read())
        elif action "w":
            modified_content = "bou"
            with open(filename, "w") as file
                file.write(modified_content)
    except Exception as err:
         return (False, str(err))

print(f"=== Cyber Archives Security ===")
print()
print(f"Using 'secure_archive' to read from a nonexistent file:")
res1 = secure_archive("/not/existing/file", "r")
print(res1)

print()
print(f"Using 'secure_archive' to read from an inaccessible file:")
res2 = secure_archive("etc/master.passw", "r")
print(res2)

print()
print(f"Using 'secure_archive' to read from a regular file:")
res3 = secure_archive("the.txt", "r")
print(res3)

print()
print(f"Using 'secure_archive' to write previous content to a new file:")
res4 = secure_archive("new_vault_file.txt", "w", res3[1])
print(res4)
        
    
