def add_numbering_to_lines_in_file(file_path: str) -> None:
    """Добавляет нумерацию к существующему файлу."""
    file = open(file_path, "r")
    lines = file.readlines()

    file = open(file_path, "w")
    for i in range(len(lines)):
        file.write(f"{i + 1}: {lines[i]}")

    file.close()


def show_file_with_line_numbering(file_path: str) -> None:
    """Выводит отредактированный файл с нумерацией для каждой строки."""
    with open(file_path, "r") as file:
        print(file.read())


def main():
    file_path = input("Введите путь к файлу: ")

    add_numbering_to_lines_in_file(file_path)
    show_file_with_line_numbering(file_path)


if __name__ == '__main__':
    main()
