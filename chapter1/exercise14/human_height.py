FROM_FOOT_TO_INCHES = 12
FROM_INCHES_TO_CENTIMETERS = 2.54

feet = float(input("Введите ваш рост (в футах): "))
inches = float(input("Введите ваш рост (в дюймах): "))

humanHeight = round(feet * FROM_FOOT_TO_INCHES * FROM_INCHES_TO_CENTIMETERS, 2)
print(f"Ваш рост (из {feet} футов) равен {humanHeight} см")

humanHeight = round(inches * FROM_INCHES_TO_CENTIMETERS, 2)
print(f"Ваш рост (из {inches} дюймов) равен {humanHeight} см")
