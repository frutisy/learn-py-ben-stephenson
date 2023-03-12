print("Первое число не должно быть равно нулю.\n"
      "Индикатором конца ввода как раз будет служить ноль.")

numbers = input("Введите числа через пробел: ").split()

if int(numbers[0]) == 0:
    raise ValueError("Первое число не должно быть нулём")

averageValue = 0
quantityNumbersBeforeZero = 0

for number in numbers:
    if int(number) == 0:
        break

    averageValue += int(number)
    quantityNumbersBeforeZero += 1

averageValue = round(averageValue / quantityNumbersBeforeZero, 2)

print(f"Среднее значение равно {averageValue}")
