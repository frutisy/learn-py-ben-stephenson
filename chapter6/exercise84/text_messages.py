PHONE_BUTTONS = {
    1: ['.', ',', '?', '!', ':'],
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z'],
    0: [' ']
}


def get_buttons(text: str) -> str:
    """Получает последовательность кнопок, которую необходимо нажать, чтобы на
    экране телефона появился текст, введённый пользователем."""
    digits = ''

    for symbol in text:
        # Перевод символа в верхний регистр во избежания пропуска строчных букв.
        symb = symbol.upper()

        for button, symbols in PHONE_BUTTONS.items():
            # Символ отсутствует в списке символов для текущей кнопки.
            if symb not in symbols:
                continue
            # Символ присутствует.
            else:
                # Определение количества нажатий на кнопку.
                number_of_button_presses = PHONE_BUTTONS[button].index(symb) + 1
                digits += str(button) * number_of_button_presses

    return digits


def main():
    text = input("Введите текст: ")
    print(f"Последовательность кнопок: {get_buttons(text)}")


if __name__ == '__main__':
    main()
