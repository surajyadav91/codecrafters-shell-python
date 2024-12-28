import sys
import os
from pathlib import Path

def main():
    # Uncomment this block to pass the first stage
    builtin_commands = ["type", "echo", "exit"]
    path_env = os.getenv('PATH')
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
            if args[1] in builtin_commands:
                print(f'{args[1]} is a shell builtin')
            
            else:
                for path in path_env.split(':'):
                    command_path = Path(path) / args[1]
                    if command_path.is_file() and os.access(command_path, os.X_OK):
                        print(f'{args[1]} is {command_path}')
                        break
                
                else:
                    print(f'{args[1]}: not found')
            
            continue


        elif command not in builtin_commands:
            print(f'{command}: command not found')
            continue

    # # Wait for user input
    # command = input()
    # print(f'{command}: command not found')


if __name__ == "__main__":
    main()
