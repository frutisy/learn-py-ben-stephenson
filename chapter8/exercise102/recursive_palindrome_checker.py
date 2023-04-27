def is_palindrome(word: str) -> bool:
    """Проверяет, является ли строка палиндромом."""
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])


def main():
    word = input("Введите слово: ")

    if is_palindrome(word):
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")


if __name__ == '__main__':
    main()
