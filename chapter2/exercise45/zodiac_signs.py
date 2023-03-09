birthday = input("Введите дату вашего рождения (например, '22 февраля'): ")

# ['22', 'февраля']
dateOfBirth = birthday.split()

day = int(dateOfBirth[0])
month = dateOfBirth[1]

# Козерог.
if (month == 'декабря' and day >= 22) or (month == 'января' and day <= 19):
    print(f"Ваш знак зодиака - Козерог")
# Водолей.
elif (month == 'января' and day >= 20) or (month == 'февраля' and day <= 18):
    print(f"Ваш знак зодиака - Водолей")
# Рыбы.
elif (month == 'февраля' and day >= 19) or (month == 'февраля' and day <= 20):
    print(f"Ваш знак зодиака - Рыбы")
# Овен.
elif (month == 'марта' and day >= 21) or (month == 'апреля' and day <= 19):
    print(f"Ваш знак зодиака - Овен")
# Телец.
elif (month == 'апреля' and day >= 20) or (month == 'мая' and day <= 20):
    print(f"Ваш знак зодиака - Телец")
# Близнецы.
elif (month == 'мая' and day >= 21) or (month == 'июня' and day <= 20):
    print(f"Ваш знак зодиака - Близнецы")
# Рак.
elif (month == 'июня' and day >= 21) or (month == 'июля' and day <= 22):
    print(f"Ваш знак зодиака - Рак")
# Лев.
elif (month == 'июля' and day >= 23) or (month == 'августа' and day <= 22):
    print(f"Ваш знак зодиака - Лев")
# Дева.
elif (month == 'августа' and day >= 23) or (month == 'сентября' and day <= 22):
    print(f"Ваш знак зодиака - Дева")
# Весы.
elif (month == 'сентября' and day >= 23) or (month == 'октября' and day <= 22):
    print(f"Ваш знак зодиака - Весы")
# Скорпион.
elif (month == 'октября' and day >= 23) or (month == 'ноября' and day <= 21):
    print(f"Ваш знак зодиака - Скорпион")
# Стрелец.
elif (month == 'ноября' and day >= 22) or (month == 'декабря' and day <= 21):
    print(f"Ваш знак зодиака - Стрелец")
