ACRE = 43560

length = float(input("Введите длину садового участка (в футах): "))
width = float(input("Введите ширину садового участка (в футах): "))

gardenPlotArea = round((length * width) / ACRE, 2)

print(f"Площадь садового участка равна {gardenPlotArea} акров")
