import sys
import typing


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO[str] = open(filename, "r")
        content: str = file.read()
        print("---")
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")
        file.close()
        print(f"File '{filename}' closed.")
    except Exception as err:
        print(f"Error opening file '{filename}': {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
