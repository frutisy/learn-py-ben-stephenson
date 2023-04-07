import sys

from typing import TextIO


def verify_for_file() -> None:
    """
    Проверяет следующие параметры:

    - количество введённых параметров;
    - корректность ввода утилиты;
    - наличие файла с расширением .txt.

    Если все параметры введены корректно, то будет вызвана функция im_head().
    В противном случае будут выведены соответствующие сообщения об ошибках.
    """
    utility_name = 'im_head'

    # Проверяем количество введённых параметров.
    if len(sys.argv) != 3:
        print("Количество аргументов должно быть равно 3.")
        print(f"К примеру, python3 '<file.py> {utility_name} <file.txt>'.")
        quit()

    # Проверяем корректность ввода утилиты.
    if sys.argv[1] == utility_name:
        file_name = sys.argv[2]
        # Проверяем наличие файла с расширением .txt.
        try:
            with open(file_name, "r") as file:
                im_head(file)
        except FileNotFoundError:
            print(f"Файла с именем {file_name} не существует.")
            quit()
    else:
        print(f"Вы ввели '{sys.argv[1]}', что не соответствует '{utility_name}'.")


def im_head(file: TextIO) -> None:
    """
    Имитация утилиты head в системах на базе Unix.

    Выводит первые десять строк содержимого файла.
    """
    lines = file.readlines()[:10]

    for line in lines:
        print(line.rstrip())


def main():
    verify_for_file()


if __name__ == '__main__':
    main()
