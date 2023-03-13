PRICE_FOR_CHILD = 0  # Дети до двух лет.
PRICE_FOR_TEENAGE = 14  # Дети от трёх до 12 лет.
PRICE_FOR_ADULT = 23  # Взрослые от 13 до 65 лет.
PRICE_FOR_PENSIONER = 18  # Пенсионеры старше 65 лет.

ages = []

age = int(input("Введите возраст: "))
ages.append(int(age))

while True:
    age = input("Введите возраст (Enter для окончания ввода): ")

    if age == '':
        break

    ages.append(int(age))

price = 0.0

for age in ages:
    if age <= 2:
        price += PRICE_FOR_CHILD
    elif 2 < age <= 12:
        price += PRICE_FOR_TEENAGE
    elif 12 < age < 65:
        price += PRICE_FOR_ADULT
    else:
        price += PRICE_FOR_PENSIONER

price = round(price, 2)

print(f"Общая цена за всех людей равна {price}$")
