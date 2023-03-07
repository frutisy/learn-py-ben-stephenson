MONTHS = {
    'January': 31,
    'February': (28, 29),
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'Jule': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

month = input("Введите название месяца: ")

for monthName, quantityOfDays in MONTHS.items():
    if month == monthName:
        print(f"{quantityOfDays} дней в {month}")
