import sys


def main():
    # Uncomment this block to pass the first stage
    valid_commands = ["type", "echo", "exit"]
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

        elif args[0] == "type":
            if args[1] in valid_commands:
                print(f'{args[1]} is a shell builtin')
            else:
                print(f'{args[1]}: not found')
            
            continue

        elif command not in valid_commands:
            print(f'{command}: command not found')
            continue

    # # Wait for user input
    # command = input()
    # print(f'{command}: command not found')


if __name__ == "__main__":
    main()
