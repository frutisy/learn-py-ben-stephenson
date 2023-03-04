INTEREST_RATE = 0.04
DEPOSIT_PERIOD = 3

depositAmount = float(input("Введите сумму начального депозита: $"))

for year in range(1, DEPOSIT_PERIOD + 1):
    depositAmount = round(depositAmount + depositAmount * INTEREST_RATE, 2)
    print(f"Сумма депозита в конце {year} года равна ${depositAmount}")
