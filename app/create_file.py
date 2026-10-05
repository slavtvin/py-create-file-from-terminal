import sys
import os
from datetime import datetime


def main():
    args = sys.argv[1:]

    directories = []
    filename = None
    i = 0

    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                directories.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
        else:
            i += 1

    dir_path = ""
    if directories:
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)

    if filename:
        file_path = os.path.join(dir_path, filename) if dir_path else filename

        file_exists = os.path.exists(file_path)

        lines = []
        line_number = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input.lower() == "stop":
                break
            lines.append(f"{line_number} {user_input}")
            line_number += 1

        with open(file_path, "a") as f:
            if file_exists and os.path.getsize(file_path) > 0:
                f.write("\n\n")

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(timestamp + "\n")

            for line in lines:
                f.write(line + "\n")


if __name__ == "__main__":
    main()