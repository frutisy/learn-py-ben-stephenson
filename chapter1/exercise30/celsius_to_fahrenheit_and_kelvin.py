TO_FAHRENHEIT1 = 1.8
TO_FAHRENHEIT2 = 32
TO_KELVIN = 273.15

temperatureInCelsius = float(input("Введите температура (в гр. Цельсия): "))

temperatureInFahrenheit = temperatureInCelsius * TO_FAHRENHEIT1 + TO_FAHRENHEIT2
temperatureInKelvin = temperatureInCelsius + TO_KELVIN

print(f"Температура в Фаренгейтах равна{temperatureInFahrenheit}")
print(f"Температура в Кельвинах равна {temperatureInKelvin}")
