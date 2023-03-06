number = int(input("Введите целое четырёхзначное число: "))

thousands = number // 1000
hundreds = (number - thousands * 1000) // 100
tens = (number - thousands * 1000 - hundreds * 100) // 10
remainder = number - thousands * 1000 - hundreds * 100 - tens * 10

amount = thousands + hundreds + tens + remainder

print(f"Сумма цифр числа {number} равна {amount}")
