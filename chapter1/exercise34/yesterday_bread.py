DISCOUNT = 0.6

todayBreadPrice = 3.49
yesterdayBreadPrice = round(todayBreadPrice * DISCOUNT, 2)

boughtYesterdayBread = int(input("Введите количество приобретённых вчерашних"
                                 "буханок хлеба: "))
cost = round(boughtYesterdayBread * yesterdayBreadPrice, 2)

print(f"Цена за сегодняшний хлеб равна ${todayBreadPrice}")
print(f"Цена за хлеб со скидкой {int(DISCOUNT * 100)}% равна ${yesterdayBreadPrice}")
print(f"Цена за {boughtYesterdayBread} вчерашних буханок хлеба равна ${cost}")
