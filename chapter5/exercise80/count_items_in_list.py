from typing import Union


def verify_bounds(min_bound: Union[int, float],
                  max_bound: Union[int, float]) -> None:
    """Проверяет корректность ввода минимальной и максимальной границ."""
    if not isinstance(min_bound, (int, float)) or not isinstance(max_bound, (int, float)):
        raise TypeError("Минимальная и максимальная границы должны "
                        "соответствовать типам int или float")

    if min_bound >= max_bound:
        raise ValueError("Минимальная граница не должна быть больше либо равна "
                         "максимальной границе")


def count_range(lst: list[int, float],
                min_bound: Union[int, float],
                max_bound: Union[int, float]) -> int:
    """Подсчитывает количество элементов в списке, значения которых больше или
    равны заданному минимальному порогу и меньше максимального.
    """
    verify_bounds(min_bound, max_bound)

    count = 0
    for item in lst:
        if min_bound <= item < max_bound:
            count += 1

    return count


def show(lst: list[int, float], min_bound: Union[int, float], max_bound: Union[int, float]) -> None:
    """Отображает список для подсчёта, минимальную границу, максимальную границу
    и результат функции count_range."""
    print(f"\nСписок: {lst}")
    print(f"min_bound = {min_bound}")
    print(f"max_bound = {max_bound}")
    print(f"count_range: {count_range(lst, min_bound, max_bound)}")


def main():
    numbers1 = [num for num in range(10)]
    min_bound = 2
    max_bound = 5
    show(numbers1, min_bound, max_bound)

    numbers2 = [num for num in range(-5, 5)]
    min_bound = -2
    max_bound = 7
    show(numbers2, min_bound, max_bound)

    numbers3 = [-3.1, -2.2, -1.3, 0, 1.3, 2.2, 3.1]
    min_bound = -8
    max_bound = 2
    show(numbers3, min_bound, max_bound)


if __name__ == '__main__':
    main()
