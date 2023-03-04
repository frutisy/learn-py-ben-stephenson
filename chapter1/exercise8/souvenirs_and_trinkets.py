SOUVENIR_WEIGHT = 75
TRINKET_WEIGHT = 112

quantitySouvenirs = int(input("Введите количество сувениров: "))
quantityTrinkets = int(input("Введите количество безделушек: "))

totalWeightParcel = (quantitySouvenirs * SOUVENIR_WEIGHT +
                     quantityTrinkets * TRINKET_WEIGHT)

print(f"Общий вес посылки равен {totalWeightParcel} г")
