FROM_FOOT_TO_INCHES = 2.54
FROM_FOOT_TO_YARDS = 0.33
FROM_FOOT_TO_MILES = 0.000189

distance = float(input("Введите расстояние (в футах): "))

distanceInInches = round(distance * FROM_FOOT_TO_INCHES, 2)
distanceInYards = round(distance * FROM_FOOT_TO_YARDS, 2)
distanceInMiles = round(distance * FROM_FOOT_TO_MILES, 2)

print(f"Расстояние в дюймах равно {distanceInInches}")
print(f"Расстояние в ярдах равно {distanceInInches}")
print(f"Расстояние в милях равно {distanceInInches}")
