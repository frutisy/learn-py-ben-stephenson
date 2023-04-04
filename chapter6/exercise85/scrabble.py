PRICE_OF_LETTERS = {
    1: 'AEILNORSTU',
    2: 'DG',
    3: 'BCMP',
    4: 'FHVWY',
    5: 'K',
    8: 'JX',
    10: 'QZ'
}


def count_points(word: str) -> int:
    """Считает количество набранных очков за собранное слово."""
    points = 0

    for letter in word.upper():
        for price, letters in PRICE_OF_LETTERS.items():
            if letter in letters:
                points += price
                break

    return points


def show_points(word: str) -> None:
    """Выводит количество набранных очков за собранное слово."""
    print(count_points(word))


def main():
    word = input("Введите слово (на английском языке): ")
    show_points(word)


if __name__ == '__main__':
    main()
