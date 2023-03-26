def is_list_sorted(lst: list) -> bool:
    """Возвращает True, если список, переданный в качестве аргумента,
    отсортирован по возрастанию или убыванию."""
    if sorted(lst) == lst or sorted(lst, reverse=True) == lst[::-1]:
        return True
    return False


def main():
    numbers = input("Введите числа (через пробел): ").split()
    numbers = [int(number) for number in numbers]

    if is_list_sorted(numbers):
        print(f"Ваш список является отсортированным")
    else:
        print(f"Ваш список не является отсортированным")


if __name__ == '__main__':
    main()
