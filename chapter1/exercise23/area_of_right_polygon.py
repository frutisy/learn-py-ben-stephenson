from math import tan
from math import pi

s = float(input("s = "))
n = float(input("n = "))

area = round((n * s**2) / (4 * tan(pi / n)), 2)

print(f"Площадь правильного многоугольника равна {area}")
