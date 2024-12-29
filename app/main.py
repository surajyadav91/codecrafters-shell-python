import sys
import os
from pathlib import Path
import subprocess

def locate_executable(command):
    path = os.getenv('PATH')
    for path in path.split(':'):
        command_path = Path(path) / command
        if command_path.is_file() and os.access(command_path, os.X_OK):
            return command_path
    return None

def main():
    # Uncomment this block to pass the first stage
    builtin_commands = ["type", "echo", "exit"]
    path_env = os.getenv('PATH')
    all_env_paths = path_env.split(':')
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()
        args = command.split()

        if command == "exit 0":
            break

        elif args[0] == "echo":
            print(" ".join(args[1:]))

        elif args[0] == "type":
            if args[1] in builtin_commands:
                print(f'{args[1]} is a shell builtin')
            
            else:
                command_path = locate_executable(args[1])
                if command_path:
                    print(f'{args[1]} is {command_path}')
                
                else:
                    print(f'{args[1]}: not found')

        elif executable_path := locate_executable(args[0]):
            # run_result = subprocess.run([executable_path, *args[1:]], capture_output=True, text=True)
            subprocess.run([executable_path, *args[1:]])


        elif command not in builtin_commands:
            print(f'{command}: command not found')

    # # Wait for user input
    # command = input()
    # print(f'{command}: command not found')


if __name__ == "__main__":
    main()
