n = int(input("Введите целое число: "))

amount = 0
for number in range(1, n + 1):
    amount += number

print(f"Сумма первых {n} положительных чисел равна {amount}")
