TIP_RATE = 0.18
TAX_RATE = 0.13

orderAmount = float(input("Введите сумму заказа: "))

tip = round(orderAmount * TIP_RATE, 2)
tax = round(orderAmount * TAX_RATE, 2)

print(f"Сумма налога равна ${tip}")
print(f"Сумма чаевых равна ${tax}")
