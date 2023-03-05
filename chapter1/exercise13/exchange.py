changeAmount = int(input("Введите сумму сдачи (в центах): "))

coinDenomination = [1, 5, 10, 25, 100, 200]

quantityOneCent = 0
quantityFiveCent = 0
quantityTenCent = 0
quantityTwentyFiveCent = 0
quantityLoonie = 0
quantityToonie = 0

while changeAmount != 0:

    if changeAmount >= coinDenomination[-1]:
        quantityToonie += 1
        changeAmount -= coinDenomination[-1]

    elif coinDenomination[-1] > changeAmount >= coinDenomination[-2]:
        quantityLoonie += 1
        changeAmount -= coinDenomination[-2]

    elif coinDenomination[-2] > changeAmount >= coinDenomination[-3]:
        quantityTwentyFiveCent += 1
        changeAmount -= coinDenomination[-3]

    elif coinDenomination[-3] > changeAmount >= coinDenomination[-4]:
        quantityTenCent += 1
        changeAmount -= coinDenomination[-4]

    elif coinDenomination[-4] > changeAmount >= coinDenomination[-5]:
        quantityFiveCent += 1
        changeAmount -= coinDenomination[-5]

    elif coinDenomination[-5] > changeAmount >= coinDenomination[-6]:
        quantityOneCent += 1
        changeAmount -= coinDenomination[-6]

coins = {
    '1 cent': quantityOneCent,
    '5 cent': quantityFiveCent,
    '10 cent': quantityTenCent,
    '25 cent': quantityTwentyFiveCent,
    'loonie': quantityLoonie,
    'toonie': quantityToonie
}

print("Заберите деньги:")
for coinFaceValue, quantityCents in coins.items():
    if quantityCents != 0:
        print(f"{coinFaceValue}: {quantityCents} монет(а/ы)")
