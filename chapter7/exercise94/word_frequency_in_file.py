from string import whitespace, punctuation

UNNECESSARY_SYMBOLS = whitespace + punctuation


def identify_frequently_used_words(file_path: str) -> dict:
    """
    Определяет слова, которые чаще остальных встречаются в текстовом файле.

    При этом пробелы и знаки препинания будут проигнорированы.
    Также не будет учитываться регистр.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
        words = []

        for line in lines:
            # Убираем символы "\n" в конце каждой из строк.
            line = line.rstrip()
            # Разбиваем строки на слова и добавляем их в список.
            words += line.split()

        for i in range(len(words)):
            # Игнорируем регистр и избавляемся от ненужных символов в слове.
            words[i] = words[i].lower().strip(UNNECESSARY_SYMBOLS)

        for word in words:
            # Удаляем символы тире в списке слов.
            if not word.isalpha():
                words.remove(word)

        word_frequency = {word: words.count(word) for word in set(words)}

        return {word: value for word, value in word_frequency.items() if value == max(word_frequency.values())}


def show_most_frequent_words(most_frequent_words: dict) -> None:
    """Выводит самые часто встречающиеся слова в файле."""
    for word in most_frequent_words:
        print(f"Часто встречающееся слово - '{word}'.")


def main():
    file_path = input("Введите путь к файлу: ")

    most_frequent_words = identify_frequently_used_words(file_path)
    show_most_frequent_words(most_frequent_words)


if __name__ == '__main__':
    main()
