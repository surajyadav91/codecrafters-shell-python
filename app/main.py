import sys


def main():
    # Uncomment this block to pass the first stage
    valid_commands = []
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()

        if command == "exit 0":
            break

        if command.split()[0] == "echo":
            print(" ".join(command.split()[1:]))
            continue

        if command not in valid_commands:
            print(f'{command}: command not found')
            continue

    # # Wait for user input
    # command = input()
    # print(f'{command}: command not found')


if __name__ == "__main__":
    main()
