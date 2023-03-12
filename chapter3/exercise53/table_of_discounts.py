DISCOUNT = 0.6

newPrices = [4.95, 9.95, 14.95, 19.95, 24.95]
oldPrices = []
discountAmounts = []

i = 0
for price in newPrices:
    oldPrice = round(price + price * DISCOUNT, 2)
    oldPrices.append(oldPrice)

    discountAmount = round(oldPrices[i] - newPrices[i], 2)
    discountAmounts.append(discountAmount)
    i += 1

for k in range(len(newPrices)):
    print(f"Old price: {oldPrices[k]}$ \t "
          f"Discount amount: {discountAmounts[k]}$ \t "
          f"New price: {newPrices[k]}")
