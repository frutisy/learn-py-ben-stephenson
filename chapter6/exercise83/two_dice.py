from random import randint


def roll_two_dice() -> int:
    """Выбрасывает две игральные шестигранные кости и возвращает их сумму."""
    first_dice = randint(1, 6)
    second_dice = randint(1, 6)
    result = first_dice + second_dice
    return result


def show_results(expected_percentage: dict, final_percentage: dict) -> None:
    """Выводит ожидаемый и итоговый результаты в виде таблицы."""
    print(f"Исход\tПроцент симуляции\tОжидаемый процент")

    for key in range(2, 13):
        if final_percentage[key] >= 10:
            print(
                f"{key}\t\t{final_percentage[key]}\t\t\t\t{expected_percentage[key]}")
        else:
            print(f"{key}\t\t{final_percentage[key]}\t\t\t\t\t{expected_percentage[key]}")


def main():
    expected_percentage = {
        2: 2.78,
        3: 5.56,
        4: 8.33,
        5: 11.11,
        6: 13.89,
        7: 16.67,
        8: 13.89,
        9: 11.11,
        10: 8.33,
        11: 5.56,
        12: 2.78
    }

    final_percentage = {
        2: 0.0,
        3: 0.0,
        4: 0.0,
        5: 0.0,
        6: 0.0,
        7: 0.0,
        8: 0.0,
        9: 0.0,
        10: 0.0,
        11: 0.0,
        12: 0.0
    }

    total_number_of_dice_rolls = 1000

    for i in range(0, total_number_of_dice_rolls):
        result = roll_two_dice()
        final_percentage[result] += 1

    for outcome, quantity_of_dice_rolls in final_percentage.items():
        final_percentage[outcome] = round((quantity_of_dice_rolls / total_number_of_dice_rolls) * 100, 2)

    show_results(expected_percentage, final_percentage)


if __name__ == '__main__':
    main()
