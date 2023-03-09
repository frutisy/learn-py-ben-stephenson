cellCoordinate = input("Введите координату клетки: ")

# a
if cellCoordinate[0] == 'a':
    print(f"Столбец '{cellCoordinate[0]}' начинается с чёрной клетки")

    a = 1
    if (int(cellCoordinate[1]) + a) % 2 == 0:
        print(f"Клетка {cellCoordinate} чёрная")
    else:
        print(f"Клетка {cellCoordinate} белая")

# b
elif cellCoordinate[0] == 'b':
    print(f"Столбец '{cellCoordinate[0]}' начинается с белой клетки")

    b = 2
    if (int(cellCoordinate[1]) + b) % 2 == 0:
        print(f"Клетка {cellCoordinate} чёрная")
    else:
        print(f"Клетка {cellCoordinate} белая")

# c
elif cellCoordinate[0] == 'c':
    print(f"Столбец '{cellCoordinate[0]}' начинается с чёрной клетки")

    c = 3
    if (int(cellCoordinate[1]) + c) % 2 == 0:
        print(f"Клетка {cellCoordinate} чёрная")
    else:
        print(f"Клетка {cellCoordinate} белая")

# d
elif cellCoordinate[0] == 'd':
    print(f"Столбец '{cellCoordinate[0]}' начинается с белой клетки")

    d = 4
    if (int(cellCoordinate[1]) + d) % 2 == 0:
        print(f"Клетка {cellCoordinate} чёрная")
    else:
        print(f"Клетка {cellCoordinate} белая")

# e
elif cellCoordinate[0] == 'e':
    print(f"Столбец '{cellCoordinate[0]}' начинается с чёрной клетки")

    e = 5
    if (int(cellCoordinate[1]) + e) % 2 == 0:
        print(f"Клетка {cellCoordinate} чёрная")
    else:
        print(f"Клетка {cellCoordinate} белая")

# f
elif cellCoordinate[0] == 'f':
    print(f"Столбец '{cellCoordinate[0]}' начинается с белой клетки")

    f = 6
    if (int(cellCoordinate[1]) + 6) % 2 == 0:
        print(f"Клетка {cellCoordinate} чёрная")
    else:
        print(f"Клетка {cellCoordinate} белая")

# g
elif cellCoordinate[0] == 'g':
    print(f"Столбец '{cellCoordinate[0]}' начинается с чёрной клетки")

    g = 7
    if (int(cellCoordinate[1]) + g) % 2 == 0:
        print(f"Клетка {cellCoordinate} чёрная")
    else:
        print(f"Клетка {cellCoordinate} белая")

# h
elif cellCoordinate[0] == 'h':
    print(f"Столбец '{cellCoordinate[0]}' начинается с белой клетки")

    h = 8
    if (int(cellCoordinate[1]) + h) % 2 == 0:
        print(f"Клетка {cellCoordinate} чёрная")
    else:
        print(f"Клетка {cellCoordinate} белая")
