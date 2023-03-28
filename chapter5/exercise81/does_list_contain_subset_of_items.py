def is_sublist(larger: list, smaller: list) -> bool:
    """
    Возвращает True, если:
    1) список smaller не пуст;
    2) список smaller содержит 1 элемент и этот элемент входит в список larger;
    3) элементы списка smaller входят в список larger и соседствуют.

    В противном случае возвращает False.
    """
    if not smaller:
        return True
    if len(smaller) == 1 and smaller[0] in larger:  #
        return True

    set_smaller = set(smaller)
    set_larger = set(larger)

    # Элементы списка smaller входят в список larger.
    if set_smaller.issubset(set_larger):
        index = larger.index(smaller[0])
        for i in range(len(smaller)):
            if smaller[i] == larger[index]:  # Элементы соседствуют.
                index += 1
                continue
            else:  # Элементы не соседствуют.
                return False
        else:  # По окончании цикла все элементы оказались "соседями".
            return True

    return False


def show_result(larger: list, smaller: list) -> None:
    """Отображает список smaller, список larger и сообщение о том, является ли
    список smaller подсписком списка larger."""
    print(f"\nСписок larger: \n{larger}")
    print(f"Список smaller: \n{smaller}")

    if is_sublist(larger, smaller):
        print(f"Список smaller является подсписком larger")
    else:
        print(f"Список smaller не является подсписком larger")


def main():
    # Основной список.
    numbers = [number for number in range(10)]

    # Списки, которые являются подсписками списка numbers:
    list1 = []
    show_result(numbers, list1)

    list2 = [5]
    show_result(numbers, list2)

    list3 = [1, 2, 3]
    show_result(numbers, list3)

    list4 = [number for number in range(10)]
    show_result(numbers, list4)

    # Списки, которые не являются подсписками списка numbers:
    list5 = [-1]
    show_result(numbers, list5)

    list6 = [2, 4, 6]
    show_result(numbers, list6)


if __name__ == '__main__':
    main()
