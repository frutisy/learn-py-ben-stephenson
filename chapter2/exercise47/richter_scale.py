magnitude = float(input("Введите магнитуду землетрясения по шкале Рихтера: "))

if magnitude < 2:
    print("Минимальный уровень землетрясения")
elif 2 <= magnitude < 3:
    print("Очень слабый уровень землетрясения")
elif 3 <= magnitude < 4:
    print("Слабый уровень землетрясения")
elif 4 <= magnitude < 5:
    print("Промежуточный уровень землетрясения")
elif 5 <= magnitude < 6:
    print("Умеренный уровень землетрясения")
elif 6 <= magnitude < 7:
    print("Сильный уровень землетрясения")
elif 7 <= magnitude < 8:
    print("Очень сильный уровень землетрясения")
elif 8 <= magnitude < 10:
    print("Огромный уровень землетрясения")
elif magnitude >= 10:
    print("Разрушительный уровень землетрясения")
