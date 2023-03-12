LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

machineNumber = input("Введите номерной знак машины: ")

for letter in machineNumber[:3]:
    if letter not in LETTERS:
        raise TypeError("Номерной знак введён неверно")

for digit in machineNumber[3:]:
    if not digit.isdigit():
        raise TypeError("Номерной знак введён неверно")

if len(machineNumber) == 6:
    print(f"Номерной знак '{machineNumber}' соответствует старому формату")
elif len(machineNumber) == 7:
    print(f"Номерной знак '{machineNumber}' соответствует новому формату")
else:
    raise TypeError("Длина номерного знака не соответствует значению 6 или 7")
