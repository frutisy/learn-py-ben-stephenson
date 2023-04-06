def count_unique_characters(text: str) -> int:
    """Считает количество уникальных символов в строке."""
    return len(set(text))


def show_number_of_unique_characters(text: str) -> None:
    """Выводит количество уникальных символов в строке."""
    print(count_unique_characters(text))


def main():
    text = input("Введите строку: ")
    show_number_of_unique_characters(text)


if __name__ == '__main__':
    main()
