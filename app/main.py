import sys


def main():
    # Uncomment this block to pass the first stage
    valid_commands = []
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()
        args = command.split()

        if command == "exit 0":
            break

        elif args[0] == "echo":
            print(" ".join(args[1:]))
            continue

        elif command not in valid_commands:
            print(f'{command}: command not found')
            continue

    # # Wait for user input
    # command = input()
    # print(f'{command}: command not found')


if __name__ == "__main__":
    main()
