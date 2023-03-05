R = 8.314

p = float(input("p = "))
v = float(input("v = "))
t = float(input("t = "))

t = t + 273.15

n = round((p * v) / (R * t), 2)

print(f"Количество газа равно {n} моль")
