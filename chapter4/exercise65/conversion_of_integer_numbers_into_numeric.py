def translate_integer_into_numeral(number: int) -> str:
    if number < 1 or number > 12:
        return ""

    if number == 1:
        return "Первый"
    if number == 2:
        return "Второй"
    if number == 3:
        return "Третий"
    if number == 4:
        return "Четвёртый"
    if number == 5:
        return "Пятый"
    if number == 6:
        return "Шестой"
    if number == 7:
        return "Седьмой"
    if number == 8:
        return "Восьмой"
    if number == 9:
        return "Девятый"
    if number == 10:
        return "Десятый"
    if number == 11:
        return "Одиннадцатый"
    if number == 12:
        return "Двенадцатый"


def main():
    for num in range(1, 13):
        print(f"{num} - {translate_integer_into_numeral(num)}")


if __name__ == '__main__':
    main()
