from datetime import datetime
import os
import sys


def parse_args() -> tuple:
    args = sys.argv[1:]

    dir_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")

        if "-f" in args:
            f_index = args.index("-f")
            dir_parts = args[d_index + 1: f_index]
            file_name = args[f_index + 1] if f_index + 1 < len(args) else None
        else:
            dir_parts = args[d_index + 1:]

    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1] if f_index + 1 < len(args) else None

    return dir_parts, file_name


def create_directory(dir_parts: list) -> str | None:
    if not dir_parts:
        return None

    dir_path = os.path.join(*dir_parts)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def write_to_file() -> list:
    lines = []
    num = 1
    while True:
        text = input(f"Enter content line {num}: ")
        if text == "stop":
            break
        lines.append(text)
        num += 1
    return lines


def open_file(dir_path: str | None, file_name: str, lines: list) -> None:
    if dir_path:
        full_path = os.path.join(dir_path, file_name)
    else:
        full_path = file_name

    file_exists = os.path.exists(full_path) and os.path.getsize(full_path) > 0

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(full_path, "a", encoding="utf-8") as file:

        if file_exists:
            file.write("\n")

        file.write(f"{timestamp}\n")

        for line_number, line in enumerate(lines, start=1):
            file.write(f"{line_number} {line}\n")


if __name__ == "__main__":
    dirs, file_name = parse_args()

    dir_path = create_directory(dirs)

    if file_name:
        lines = write_to_file()
        open_file(dir_path, file_name, lines)
        print("Файл успішно створено!")
    else:
        print("Помилка: не вказано назву файлу (використовуйте -f).")
