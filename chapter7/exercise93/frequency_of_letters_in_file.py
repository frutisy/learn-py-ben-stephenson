import sys

from typing import TextIO
from pprint import pprint
from string import whitespace, punctuation, digits

UNNECESSARY_SYMBOLS = whitespace + punctuation + digits


def verify_for_file() -> None:
    """
    Проверяет следующие параметры:

    - количество введённых параметров;
    - наличие файла с расширением .txt.

    Если все параметры введены корректно, то будет вызвана функция decode_text().
    В противном случае будут выведены соответствующие сообщения об ошибках.
    """
    # Проверяем количество введённых параметров.
    if len(sys.argv) != 2:
        print("Количество аргументов должно быть равно 2.")
        print(f"К примеру, python3 '<file.py> <file.txt>'.")
        quit()

    file_name = sys.argv[1]

    # Проверяем наличие файла с расширением .txt.
    try:
        with open(file_name, "r") as file:
            pprint(decode_text(file))
    except FileNotFoundError:
        print(f"Файла с именем {file_name} не существует.")
        quit()


def decode_text(file: TextIO) -> dict:
    """
    Дешифрует текст путем вывода на экран частоты появления разных букв.

    При этом пробелы, знаки препинания и цифры будут проигнорированы.
    Также не будет учитываться регистр.
    """
    lines = file.readlines()
    words = []

    for line in lines:
        # Убираем символы "\n" в конце каждой из строк.
        line = line.rstrip()
        # Разбиваем строки на слова и добавляем их в список.
        words += line.split()

    letters = []

    for i in range(len(words)):
        # Игнорируем регистр и избавляемся от ненужных символов в слове.
        words[i] = words[i].lower().strip(UNNECESSARY_SYMBOLS)

        for letter in words[i]:
            # Исключаем добавление дефисов в список букв.
            if letter.isalpha():
                # Добавляем буквы сразу в нижнем регистре.
                letters.append(letter.lower())

    file.close()

    return {letter: letters.count(letter) for letter in set(letters)}


def main():
    verify_for_file()


if __name__ == '__main__':
    main()
