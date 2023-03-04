PRICE_PER_BOTTLE_LESS_ONE_LITER = 0.10
PRICE_PER_BOTTLE_OVER_ONE_LITER = 0.25

bottlesLessOneLiter = int(
    input("Введите количество бутылок, объем которых меньше 1 л: "))
bottlesOverOneLiter = int(
    input("Введите количество бутылок, объем которых больше 1 л: "))

revenue = round(bottlesLessOneLiter * PRICE_PER_BOTTLE_LESS_ONE_LITER +
                bottlesOverOneLiter * PRICE_PER_BOTTLE_OVER_ONE_LITER, 2)

print(f"Вы заработали ${revenue} за проданные бутылки")
