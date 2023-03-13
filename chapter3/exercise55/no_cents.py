prices = []

price = input("Введите цену: ")
prices.append(int(price))

while True:
    price = input("Введите цену (Enter для окончания ввода): ")

    if price == '':
        break

    prices.append(int(price))

amountOfPrices = sum(prices)

print(f"Сумма всех введённых вами цен равна {amountOfPrices / 100}$")

if amountOfPrices % 10 < 5:
    amountOfPrices = amountOfPrices - (amountOfPrices % 10)
else:
    amountOfPrices = amountOfPrices + (10 - amountOfPrices % 10)

print(f"Сумма всех введённых вами при оплате наличными {amountOfPrices / 100}$")
