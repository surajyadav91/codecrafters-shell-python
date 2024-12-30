import sys
import os
from pathlib import Path
import subprocess
import shlex

def locate_executable(command):
    path = os.getenv('PATH')
    for path in path.split(':'):
        command_path = Path(path) / command
        if command_path.is_file() and os.access(command_path, os.X_OK):
            return command_path
    return None

def process_redirect(inp):
    # inp = shlex.split(inp)
    # inp = " ".join(inp)

    if '1>' in inp:
        command, output_file = inp.split('1>')
        return command, output_file, None
    elif '2>' in inp:
        command, output_file = inp.split('2>')
        return command, None, output_file
    elif '>' in inp:
        command, output_file = inp.split('>')
        return command, output_file, None
    else:
        return inp, None, None
    
def write_to_file(output_file, msg):
    with open(output_file, 'w') as f:
        f.write(msg)


def main():
    # Uncomment this block to pass the first stage
    builtin_commands = ["type", "echo", "exit", "pwd", "cd"]
    path_env = os.getenv('PATH')
    all_env_paths = path_env.split(':')

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()
        args, output_file, error_file = process_redirect(command)
        args = args.strip()
        command = args
        if output_file:
            output_file = output_file.strip()
        if error_file:
            error_file = error_file.strip()
        args = shlex.split(args)
    
        if command == "exit 0":
            break

        elif command.startswith("echo "):
            msg = command[5:]
            if msg.startswith("'") and msg.endswith("'"):
                msg = msg[1:-1]
                if output_file:
                    write_to_file(output_file, msg + "\n")
                elif error_file:
                    write_to_file(error_file, "")
                    print(msg)
                else:
                    print(msg)
            else:
                if output_file:
                    write_to_file(output_file, " ".join(shlex.split(msg) + "\n"))
                else:
                    print(" ".join(shlex.split(msg)))

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

            if output_file:
                with open(output_file, "w") as f:
                    subprocess.run([executable_path, *args[1:]], stdout=f)
            elif error_file:
                with open(error_file, "w") as f:
                    subprocess.run([executable_path, *args[1:]], stderr=f)
            else:
                subprocess.run([executable_path, *args[1:]])

        elif args[0] == "pwd":
            print(Path.cwd().resolve())

        elif args[0] == "cd":
            ## expanduser() takes care of ~
            change_path = Path(args[1]).expanduser().resolve()

            if change_path.exists():
                os.chdir(change_path)
            else:
                print(f'cd: {change_path}: No such file or directory')
                
        else:
            print(f'{command}: command not found')

    # # Wait for user input
    # command = input()
    # print(f'{command}: command not found')


if __name__ == "__main__":
    main()
