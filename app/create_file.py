from datetime import datetime
import os
import sys


def parse_args() -> tuple[list[str], str | None]:
    args = sys.argv[1:]
    directories = []
    filename = None

    current_mode = None

    for arg in args:
        if arg == "-d":
            current_mode = "dir"
            continue
        elif arg == "-f":
            current_mode = "file"
            continue

        if current_mode == "dir":
            directories.append(arg)
        elif current_mode == "file":
            filename = arg
            current_mode = None

    return directories, filename


def main() -> None:
    directories, filename = parse_args()

    dir_path = ""
    if directories:
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)

    if not filename:
        return

    if dir_path:
        file_path = os.path.join(dir_path, filename)
    else:
        file_path = filename

    lines = []
    line_num = 1
    while True:
        try:
            user_input = input("Enter content line: ")
        except EOFError:
            break

        if user_input == "stop":
            break
        lines.append(f"{line_num} {user_input}")
        line_num += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", encoding="utf-8") as f:
        if file_exists:
            f.write("\n")
        f.write(timestamp + "\n")
        if lines:
            f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
