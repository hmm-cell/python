def secure_archive(
    filename: str, action: str = "r", content_w: str = ""
) -> tuple[bool, str]:
    try:
        if action == "r":
            with open(filename, "r") as file:
                return (True, file.read())
        elif action == "w":
            with open(filename, "w") as file:
                file.write(content_w)
            return (True, "Content successfully written to file")
        else:
            return (False, f"Invalid action '{action}'")
    except Exception as err:
        return (False, str(err))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    res1: tuple[bool, str] = secure_archive("/not/existing/file", "r")
    print(res1)

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    res2: tuple[bool, str] = secure_archive("/etc/master.passwd", "r")
    print(res2)

    print("\nUsing 'secure_archive' to read from a regular file:")
    res3: tuple[bool, str] = secure_archive("the.txt", "r")
    print(res3)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    res4: tuple[bool, str] = secure_archive("new_vault_file.txt", "w", res3[1])
    print(res4)


if __name__ == "__main__":
    main()
