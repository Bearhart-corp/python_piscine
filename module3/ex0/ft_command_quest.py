import sys


def main():
    print("=== Command Quest ===")
    len_arg = len(sys.argv)
    if len_arg == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if len_arg != 1:
        print(f"Argument{'s' * (len_arg > 1)} received: {len_arg - 1}")
    for i in range(1, len_arg):
        print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {len_arg}")


if __name__ == "__main__":
    main()
