while True:
    quantityOfSides = int(input("Введите количество сторон в диапазоне [3; 10]: "))

    if quantityOfSides < 3 or quantityOfSides > 10:
        print("Количество сторон должно находиться в диапазоне [3; 10]")
    else:
        break

if quantityOfSides == 3:
    print(f"Это треугольник")
elif quantityOfSides == 4:
    print(f"Это прямоугольник или квадрат")
elif quantityOfSides == 5:
    print(f"Это пентагон")
elif quantityOfSides == 6:
    print(f"Это гексагон")
elif quantityOfSides == 7:
    print(f"Это гептагон")
elif quantityOfSides == 8:
    print(f"Это октагон")
elif quantityOfSides == 9:
    print(f"Это девятиугольник")
elif quantityOfSides == 10:
    print(f"Это декагон")
