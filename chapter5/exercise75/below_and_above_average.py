numbers = []

number = input("Введите целое число (Enter для окончания ввода): ")

if number == '':
    raise ValueError("Вы не совершили ввод чисел")

numbers.append(int(number))

while True:
    number = input("Введите целое число: ")
    if number == '':
        break
    numbers.append(int(number))

averageValue = round(sum(numbers) / len(numbers), 2)
numbersBelowAverage = [num for num in numbers if num <= averageValue]
numbersAboveAverage = [num for num in numbers if num > averageValue]

print(f"Среднее значение равно {averageValue}")
print(f"Значения ниже среднего либо равные ему: {numbersBelowAverage}")
print(f"Значения выше среднего: {numbersAboveAverage}")
