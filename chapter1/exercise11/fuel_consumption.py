KILOMETERS_PER_MILE = 1.609
LITERS_PER_GALLON = 3.785

milesPerGallon = int(input("Введите показатель потребления топлива автомобилем"
                           "(в милях/галон): "))

litersPerHundredKilometers = round((100 * LITERS_PER_GALLON) /
                                   (milesPerGallon * KILOMETERS_PER_MILE), 2)

print(f"Показатель потребления топлива автомобилем (в л/100 км) равен"
      f"{litersPerHundredKilometers}")
