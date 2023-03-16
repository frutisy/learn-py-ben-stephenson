def compute_median(a: int, b: int, c: int) -> int:
    return sorted((a, b, c))[1]


number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))

median = compute_median(number1, number2, number3)

print(f"Медианой чисел {number1}, {number2} и {number3} является {median}")
