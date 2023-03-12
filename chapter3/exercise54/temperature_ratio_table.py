celsiusTemperatures = [t for t in range(101) if t % 10 == 0]
fahrenheitTemperatures = [((t * 9 / 5) + 32) for t in celsiusTemperatures]

print("Таблица соотношения температур Цельсия и Фаренгейта")
for k in range(len(celsiusTemperatures)):
    print(f"{celsiusTemperatures[k]} C \t{fahrenheitTemperatures[k]} F")
