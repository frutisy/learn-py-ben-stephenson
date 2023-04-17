from typing import TextIO


def remove_comments(file_path: str) -> list[str]:
    """Удаляет строки, начинающиеся с символа '#', из переданного файла."""
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Убираем символы "\n" в конце каждой из строк.
        lines = [line.rstrip() for line in lines]
        # Добавляем строки, которые не начинаются с символа '#'.
        lines = [line for line in lines if not line.lstrip().startswith('#')]

        return lines


def create_file_without_comments(path_to_new_file: str, lines: list[str]) -> TextIO:
    """Создаёт новый файл, в котором нет строк, начинающихся с символа '#'."""
    with open(path_to_new_file, 'w') as file:
        for line in lines:
            file.write(line + '\n')
        return file


def show_file(file_path: str) -> None:
    """Выводит содержимое файла."""
    print()
    print('-' * 115, '\n')

    with open(file_path, 'r') as file:
        print(file.read())


def main():
    source_file_name = input("Введите имя файла источника (расширение - .txt): ")

    # Проверяет, является файл источник текстовым файлом.
    while not source_file_name.endswith('.txt'):
        print("Файл должен иметь расширение '.txt'.")
        new_file_name = input("Введите имя файла источника: ")

    source_file_path = 'files/' + source_file_name

    # Проверяет существование файла источника.
    while True:
        try:
            file = open(source_file_path, 'r')
            break
        except FileNotFoundError:
            print(f"Файл {source_file_path} не найден.")
            file_path = input("Введите путь к файлу: ")

    output_file_name = input("Введите имя файла назначения (расширение - .txt): ")

    # Проверяет, является файл назначения текстовым файлом.
    while not output_file_name.endswith('.txt'):
        print("Файл должен иметь расширение '.txt'.")
        output_file_name = input("Введите имя нового файла: ")

    output_file_path = "files/" + output_file_name

    lines = remove_comments(source_file_path)
    new_file = create_file_without_comments(output_file_path, lines)

    show_file(source_file_path)
    show_file(output_file_path)


if __name__ == '__main__':
    main()
