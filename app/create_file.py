import sys
import os
from datetime import datetime


def main() -> None:
    directories = []
    filename = None

    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-d":
            i += 1
            while i < len(sys.argv) and not sys.argv[i].startswith("-"):
                directories.append(sys.argv[i])
                i += 1
        elif sys.argv[i] == "-f":
            i += 1
            if i < len(sys.argv):
                filename = sys.argv[i]
                i += 1
        else:
            i += 1

    if directories:
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = ""

    if filename:
        file_path = os.path.join(dir_path, filename) if dir_path else filename
    else:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [timestamp]
    line_num = 1

    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        lines.append(f"{line_num} {user_input}")
        line_num += 1

    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode) as f:
        if mode == "a" and os.path.getsize(file_path) > 0:
            f.write("\n\n")
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
