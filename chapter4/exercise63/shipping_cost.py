def compute_shipping_cost(number_of_products: int) -> float:
    price_for_first_product = 10.95
    price_for_following_products = 2.95

    shipping_cost = 0

    if number_of_products == 1:
        return price_for_first_product

    for k in range(1, number_of_products + 1):
        if k == 1:
            shipping_cost += price_for_first_product
        else:
            shipping_cost += price_for_following_products

    return round(shipping_cost, 2)


numberOfProducts = int(input("Введите количество купленных товаров: "))

shippingCost = compute_shipping_cost(numberOfProducts)

print(f"Сумма доставки составляет ${shippingCost}")
