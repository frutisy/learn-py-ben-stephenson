from math import pi

r = float(input("r = "))
h = float(input("h = "))

cylinderVolume = round(pi * r**2 * h, 1)

print(f"Объём цилиндра равен {cylinderVolume}")
