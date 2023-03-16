def verify_date(day: int, month: int, year: int) -> None:
    if type(day) != int or type(month) != int or type(year) != int:
        raise TypeError("День, месяц и год должны быть целыми числами")

    if day < 1 or day > 31:
        raise ValueError("День должен быть в диапазоне [1; 31]")
    if month < 1 or month > 12:
        raise ValueError("Месяц должен быть в диапазоне [1; 12]")
    if year < 1:
        raise ValueError("Год должен быть больше 0")


def ordinal_date(day: int, month: int, year: int) -> int:
    days_in_month = {
        1: 31,
        2: (28, 29),
        3: 31,
        4: 30,
        5: 30,
        6: 31,
        7: 30,
        8: 31,
        9: 31,
        10: 31,
        11: 30,
        12: 31
    }

    quantity_days = day

    for k in range(1, month):
        # Год не високосный и месяц - февраль (28 дней).
        if year % 4 != 0 and k == 2:
            quantity_days += int(days_in_month[k][0])
        # Год високосный и месяц - февраль (29 дней).
        elif year % 4 == 0 and k == 2:
            quantity_days += int(days_in_month[k][1])
        else:
            quantity_days += days_in_month[k]

    return quantity_days


def main():
    day = int(input("Введите день: "))
    month = int(input("Введите месяц: "))
    year = int(input("Введите год: "))

    verify_date(day, month, year)

    ordinal_number = ordinal_date(day, month, year)

    print(f"Порядковый номер введённой вами даты - {ordinal_number}")


if __name__ == '__main__':
    main()
