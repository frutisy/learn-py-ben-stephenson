day = int(input("Введите номер дня (например, '11'): "))
month = input("Введите название месяца (например, 'августа'): ")

date = str(day) + ' ' + month

# Зима.
if (month == 'декабря' and day >= 21) or (month == 'января') or \
        (month == 'февраля') or (month == 'марта' and day < 20):
    print(f"Дате '{date}' соответствует сезон 'Зима'")

# Весна.
elif (month == 'марта' and day >= 20) or (month == 'апреля') or \
        (month == 'мая') or (month == 'июня' and day < 21):
    print(f"Дате '{date}' соответствует сезон 'Весна'")

# Лето.
elif (month == 'июня' and day >= 21) or (month == 'июля') or \
        (month == 'августа') or (month == 'сентября' and day < 22):
    print(f"Дате '{date}' соответствует сезон 'Лето'")

# Осень.
elif (month == 'сентября' and day >= 22) or (month == 'октября') or \
        (month == 'ноября') or (month == 'декабря' and day < 21):
    print(f"Дате '{date}' соответствует сезон 'Осень'")
