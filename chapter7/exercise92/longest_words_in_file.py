from string import punctuation, whitespace

UNNECESSARY_SYMBOLS = punctuation + whitespace


def find_length_of_longest_word_in_file(file_path: str) -> int:
    """Находит длину самого длинного слова в файле."""
    words = []

    with open(file_path, "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.rstrip()
            words.extend(line.split())

    words = set(words)  
    max_word_length = 0

    for word in words:
        word = word.strip(UNNECESSARY_SYMBOLS)

        if len(word) > max_word_length:
            max_word_length = len(word)

    return max_word_length


def find_longest_words_in_file(file_path: str) -> list[str]:
    """Находит самые длинные слова в файле."""
    words = []

    with open(file_path, "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            words += line.split()

    words = set(words)  
    max_word_length = find_length_of_longest_word_in_file(file_path)
    longest_words = []

    for word in words:
        word = word.strip(UNNECESSARY_SYMBOLS)

        if len(word) == max_word_length:
            longest_words.append(word)

    return longest_words


def show_max_word_length_and_longest_words(max_word_length: int, 
                                           longest_words: list[str]) -> None:
    """Выводит длину самого длина слова и все слова такой длины."""
    print(f"Длина самого длинного слова равна {max_word_length}")
    print(f"Список слов такой длины: {longest_words}")


def main():
    file_path = 'files/poem.txt'

    max_word_length = find_length_of_longest_word_in_file(file_path)
    longest_words = find_longest_words_in_file(file_path)

    show_max_word_length_and_longest_words(max_word_length, longest_words)


if __name__ == '__main__':
    main()
