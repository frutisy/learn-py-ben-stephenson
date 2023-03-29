from typing import Any


def reverse_lookup(dictionary: dict, value: Any) -> list:
    """Возвращает список ключей в словаре по заданному значению."""
    keys = []

    for key in dictionary.keys():
        if dictionary[key] == value:
            keys.append(key)

    return keys


def show(dictionary: dict, value: Any) -> None:
    """Отображает словарь и найденные ключи."""
    print(f"\nСловарь: {dictionary}")
    print(f"Ключи: {reverse_lookup(dictionary, value)}")


def main():
    value = '1'
    dict1 = {
        1: '1',
        2: '2',
        3: '3',
        4: '1',
        (1, 4): '1',
        '1': '1'
    }
    show(dict1, value)

    value = '2000 г.'
    dict2 = {
        'Иванов': '2000 г.',
        'Петров': '1999 г.',
        'Сидоров': '2001 г.'
    }
    show(dict2, value)

    value = [1, 2, 3]
    show(dict2, value)


if __name__ == '__main__':
    main()
