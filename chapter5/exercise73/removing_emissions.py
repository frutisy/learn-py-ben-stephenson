from copy import copy


def verify_n_max_min(nums: list, n_max: int, n_min: int) -> None:
    lst = copy(nums)
    if n_max + n_min > len(lst):
        raise ValueError("Превышены введённые значения n для удаления")


def remove_extreme_values(nums: list, n_max: int, n_min: int) -> list:
    verify_n_max_min(nums, n_max, n_min)

    lst = copy(nums)

    for i in range(n_max):
        max_value = max(lst)
        lst.remove(max_value)

    for i in range(n_min):
        min_value = min(lst)
        lst.remove(min_value)

    return lst


numbers = []

number = int(input("Введите целочисленное значение (0 - для завершения): "))
numbers.append(number)

while number != 0:
    number = int(input("Введите целочисленное значение: "))
    numbers.append(number)
else:
    numbers.remove(0)
    if len(numbers) < 4:
        raise ValueError("Вы ввели меньше четырёх чисел")


nmax = int(input("nmax = "))
nmin = int(input("nmin = "))

newNumbers = remove_extreme_values(numbers, nmax, nmin)

print(f"Старый список: {numbers}")
print(f"Новый список: {newNumbers}")
