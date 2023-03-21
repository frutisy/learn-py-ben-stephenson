numbers = []

number = int(input("Введите целочисленное значение (0 - для завершения): "))
numbers.append(number)

while number != 0:
    number = int(input("Введите целочисленное значение: "))
    numbers.append(number)

numbers.remove(0)

for num in sorted(numbers, reverse=False):
    print(num)
