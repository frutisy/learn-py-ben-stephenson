TO_PSI = 0.14503773773022
TO_MM_MERCURY_COLUMN = 7.5006375541921

pressureInKiloPa = float(input("Введите давление (в кПа): "))

pressureInPSI = round(pressureInKiloPa * TO_PSI, 2)
pressureInMercuryColumn = round(pressureInKiloPa * TO_MM_MERCURY_COLUMN, 2)

print(f"Давление в PSI равно {pressureInPSI}")
print(f"Давление в мм. рт. столба равно {pressureInMercuryColumn}")
