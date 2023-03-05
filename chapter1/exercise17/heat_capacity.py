C = 4.186

# Первая часть задания.

m = float(input("m = "))
deltaT = float(input("deltaT = "))

q = round(m * C * deltaT, 2)

print(f"q = {q} Дж")

# Вторая часть задания.

FROM_JOULES_TO_KWH = 3600000
COST_PER_KWH = 8.9

cost = round((q * COST_PER_KWH) / FROM_JOULES_TO_KWH, 2)

print(f"Стоимость подогрева одной чашки кофе за время {deltaT} с "
      f"равна {cost} центам")
