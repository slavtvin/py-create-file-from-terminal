from datetime import datetime
import os
import sys


def parse_args() -> tuple[list[str], str | None]:
    args = sys.argv[1:]
    directories = []
    filename = None

    if "-d" in args:
        d_idx = args.index("-d")
        if "-f" in args:
            f_idx = args.index("-f")
            if d_idx < f_idx:
                directories = args[d_idx + 1 : f_idx]
            else:
                directories = args[d_idx + 1 :]
        else:
            directories = args[d_idx + 1 :]
        directories = [d for d in directories if not d.startswith("-")]

    if "-f" in args:
        f_idx = args.index("-f")
        if f_idx + 1 < len(args):
            potential_file = args[f_idx + 1]
            if not potential_file.startswith("-"):
                filename = potential_file

        if "-d" in args:
            d_idx = args.index("-d")
            if d_idx > f_idx:
                directories = args[d_idx + 1 :]
                directories = [d for d in directories if not d.startswith("-")]

    return directories, filename


def main() -> None:
    directories, filename = parse_args()

    dir_path = os.path.join(*directories) if directories else ""
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if not filename:
        return

    file_path = os.path.join(dir_path, filename) if dir_path else filename

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

    file_dir = os.path.dirname(file_path)
    if file_dir:
        os.makedirs(file_dir, exist_ok=True)

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
