def find_vowel_order_words(filename: str) -> list[str]:
    """
    Ищет слова, содержащие гласные буквы в том порядке, в котором они
    расположены в алфавите, а именно A, E, I, O, U и Y.
    """
    vowels = 'aeiouy'
    new_words = []

    with open('files/' + filename, 'r') as f:
        # Считываем все слова из файла.
        words = f.read().split()

        for word in words:
            i = 0

            for letter in word:
                # Буква гласная и идёт по порядку.
                if letter in vowels and letter == vowels[i]:
                    i += 1
                # Порядок гласных букв нарушен.
                elif letter in vowels and letter != vowels[i]:
                    break
                # Буква является согласной.
                else:
                    continue
            else:
                new_words.append(word)

    return new_words


def main():
    filename = input("Введите имя файла: ")

    # Проверяем существование файла.
    while True:
        try:
            with open('files/' + filename):
                break
        except FileNotFoundError:
            print(f"Файл {filename} не существует. Попробуйте ещё раз.")
            filename = input("Введите имя файла: ")

    print("Слова, содержащие гласные буквы, расположенные в алфавитном порядке: ")
    print(*find_vowel_order_words(filename))


if __name__ == '__main__':
    main()
