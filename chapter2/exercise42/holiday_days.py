canadianHolidays = {
    'Новый год': '1 января',
    'День Канады': '1 июля',
    'Рождество': '25 декабря'
}

day = input("Введите день праздника (например, '1'): ")
month = input("Введите месяц праздника (например, 'января'): ")

date = day + ' ' + month

if date not in canadianHolidays.values():
    print("В ведённую вами дату праздника нет")
else:
    for holidayName, holidayDate in canadianHolidays.items():
        if date == holidayDate:
            print(f"{date} праздник '{holidayName}'")
