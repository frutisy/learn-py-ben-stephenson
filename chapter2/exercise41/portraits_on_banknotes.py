banknotesUSA = {
    'Джордж Вашингтон': 1,
    'Томас Джефферсон': 2,
    'Авраам Линкольн': 5,
    'Александр Гамильтон': 10,
    'Эндрю Джексон': 20,
    'Улисс Грант': 50,
    'Бенджамин Франклин': 100
}

denomination = int(input("Введите номинал банкноты США: "))

if denomination not in banknotesUSA.values():
    print("Такой банкноты не существует")
else:
    for name, denom in banknotesUSA.items():
        if denomination == denom:
            print(f"На банкноте с номиналом ${denomination} изображён {name}")
