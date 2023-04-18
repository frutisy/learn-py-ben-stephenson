from random import randint


def create_password(file_path: str) -> str:
    """
    Создаёт пароль из файла со списком слов, где случайным образом выбирает два
    слова и сцепляет их вместе для получения итогового пароля.

    Пароль создаётся, исходя из следующих требований:
    - он должен состоять минимум из восьми и максимум из десяти символов;
    - каждое из используемых слов должно быть длиной хотя бы в три буквы;
    - необходимо сделать первые буквы двух сцепляемых слов заглавными.
    """
    with open(file_path, 'r') as file:
        words = []

        for word in file.readlines():
            word = word.rstrip()

            if 3 <= len(word) <= 7:
                words.append(word)

        first_word = words[randint(0, len(words))].capitalize()

        password = first_word
        while len(password) < 8 or len(password) > 10:
            second_word = words[randint(0, len(words))].capitalize()
            password += second_word

        return password


def main():
    file_path = 'files/words.txt'

    password = create_password(file_path)
    print(f"Сгенерированный пароль: {password}")


if __name__ == '__main__':
    main()
