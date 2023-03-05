from math import pi

r = float(input("r = "))

area = round(pi * r**2, 2)
volume = round((4 * pi * r**3) / 3, 2)

print(f"Площадь круга с радиусом {r} равна {area}")
print(f"Объём шара с радиусом {r} равен {volume}")
