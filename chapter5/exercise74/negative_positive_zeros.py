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

negativeNumbers = []
zeros = []
positiveNumbers = []

for num in numbers:
    if num < 0:
        negativeNumbers.append(num)
    elif num > 0:
        positiveNumbers.append(num)
    else:
        zeros.append(num)

newNumbers = []
newNumbers.extend(negativeNumbers)
newNumbers.extend(zeros)
newNumbers.extend(positiveNumbers)

for num in newNumbers:
    print(num)
