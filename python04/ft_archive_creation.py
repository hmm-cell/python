import sys
import typing


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO[str] = open(filename, "r")
        content: str = file.read()
        file.close()

        print("---")
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")
        print(f"File '{filename}' closed.")
    except Exception as err:
        print(f"Error opening file '{filename}': {err}")
        sys.exit(1)

    modified_content: str = ""
    if content:
        content_clean: str = content[:-1] if content.endswith("\n") else content
        lines: list[str] = content_clean.split("\n")

        for line in lines:
            modified_content += line + "#\n"

        if not content.endswith("\n"):
            modified_content = modified_content[:-1]

    print("Transform data:")
    print("---")
    print(modified_content, end="" if modified_content.endswith("\n") else "\n")
    print("---")

    new_filename: str = input("Enter new file name (or empty): ")

    if new_filename == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")

    try:
        out_file: typing.IO[str] = open(new_filename, "w")
        out_file.write(modified_content)
        out_file.close()
        print(f"Data saved in file '{new_filename}'.")
    except Exception as err:
        print(f"Error saving file '{new_filename}': {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
