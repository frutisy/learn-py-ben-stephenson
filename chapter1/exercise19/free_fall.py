from math import sqrt

VI = 0
A = 9.8
D = 5

h = float(input("Введите высоту: "))

vf = round(sqrt(VI**2 + 2 * A * D), 2)

print(f"Скорость при соприкосновении объекта с землёй равна {vf}")
