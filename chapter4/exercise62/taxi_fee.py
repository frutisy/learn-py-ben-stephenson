BASE_RATE = 4.00
FLOATING_RATE = 0.25


def compute_taxi_fee(distance: int) -> float:
    return round(BASE_RATE + distance // 140 * FLOATING_RATE, 2)


dist = 560
taxiFee = compute_taxi_fee(dist)

print(f"Сумма поездки составила ${taxiFee}")
