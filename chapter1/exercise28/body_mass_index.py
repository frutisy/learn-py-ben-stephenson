height = int(input("Введите ваш рост (в дюймах): "))
weight = float(input("Введите ваш вес (в фунтах): "))

BMI = round((weight / height**2) * 703, 2)

print(f"Ваш индекс массы тела равен {BMI}")

print()

height = int(input("Введите ваш рост (в см): "))
weight = float(input("Введите ваш вес (в кг): "))

BMI = round((weight * 10000) / height**2, 2)

print(f"Ваш индекс массы тела равен {BMI}")
