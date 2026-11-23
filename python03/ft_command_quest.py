import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
        for idx, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {idx}: {arg}")
    else:
        print("No arguments provided!")

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
