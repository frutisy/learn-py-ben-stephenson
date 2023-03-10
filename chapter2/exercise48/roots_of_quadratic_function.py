from math import sqrt

while True:
    a = float(input("a = "))
    if a != 0:
        break

b = float(input("b = "))
c = float(input("c = "))

discriminant = b**2 - 4 * a * c

if discriminant > 0:
    root = round((-b - sqrt(discriminant)) / (2 * a), 2)
    print(f"x1 = {root}")
    root = round((-b + sqrt(discriminant)) / (2 * a), 2)
    print(f"x2 = {root}")
elif discriminant == 0:
    root = (-b) / (2 * a)
else:
    print("Уравнение не имеет действительных корней")
