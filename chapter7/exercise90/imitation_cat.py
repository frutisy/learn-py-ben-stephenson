import sys


def verify_for_file() -> list:
    """
    Проверяет следующие параметры:
    - количество введённых параметров;
    - корректность ввода утилиты;
    - наличие файлов с расширениями .txt.

    Если все параметры введены корректно, то будет возвращён список file_names.
    В противном случае будут выведены соответствующие сообщения об ошибках.
    """
    utility_name = 'im_cat'

    # Проверяем количество введённых параметров.
    if len(sys.argv) < 4:
        print("Количество аргументов не должен быть меньше .")
        print(f"К примеру, python3 '<file.py> {utility_name} <file1.txt> <file2.txt> ... <fileN.txt>'.")
        quit()

    file_names = []

    # Проверяем корректность ввода утилиты.
    if sys.argv[1] == utility_name:
        # Проверяем наличие файлов с расширениями .txt.
        for file_name in sys.argv[2:]:
            try:
                with open(file_name, "r") as file:
                    file_names.append(file_name)
            except FileNotFoundError:
                print(f"ВНИМАНИЕ! Файла с именем {file_name} не существует.")
    else:
        print(f"Вы ввели '{sys.argv[1]}', что не соответствует '{utility_name}'.")

    return file_names


def im_cat(file_names: list) -> None:
    """
    Имитация утилиты cat в системах на базе Unix.

    Выводит объединённое содержимое нескольких файлов.
    """
    shared_file = open("files/shared_file.txt", "w")

    for file_name in file_names:
        with open(file_name, "r") as file:
            # Объединяем существующие файлы в один файл.
            shared_file.write(file.read() + '\n')

    shared_file = open("files/shared_file.txt", "r")

    for line in shared_file.readlines():
        print(line.rstrip())

    shared_file.close()


def main():
    file_names = verify_for_file()
    im_cat(file_names)


if __name__ == '__main__':
    main()
