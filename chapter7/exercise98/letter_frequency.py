from string import ascii_lowercase, punctuation


def get_letter_frequency(file_path: str) -> dict[str, int]:
    """
    Считывает список слов из файла и возвращает частоту появления каждой буквы
    алфавита в процентах.

    Знаки пунктуации и регистр символов будут проигнорированы.
    """
    letter_frequency = {letter: 0 for letter in ascii_lowercase}

    with open(file_path, 'r') as file:
        words = file.read().split()

        # Убираем знаки пунктуации и приводим символы к нижнему регистру.
        words = [word.lower().strip(punctuation) for word in words]

        number_of_all_letters = 0

        for word in words:
            for letter in word:
                letter_frequency[letter] += 1
                number_of_all_letters += 1

        for letter, value in letter_frequency.items():
            letter_frequency[letter] = round(value / number_of_all_letters, 2) * 100

        return letter_frequency


def show_statistic(letter_frequency: dict[str, int]) -> None:
    """
    Выводит на экран частоту появления каждой буквы алфавита и самые редко
    встречающиеся буквы.
    """
    print("Частота появления каждой буквы алфавита:")

    for letter, frequency in letter_frequency.items():
        print(f"{letter}: {frequency}%")

    min_frequency = min(letter_frequency.values())

    print("Самые редкие буквы:")

    for letter, frequency in letter_frequency.items():
        if frequency == min_frequency:
            print(letter, end=', ')


def main():
    file_path = 'files/words.txt'

    letter_frequency = get_letter_frequency(file_path)
    show_statistic(letter_frequency)


if __name__ == '__main__':
    main()
