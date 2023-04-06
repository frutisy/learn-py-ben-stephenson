from string import ascii_uppercase, digits


symbols = ascii_uppercase + digits
codes = ('.–', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
         '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
         '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----',
         '.----', '..---', '...--', '....-', '.....', '-....', '--...',
         '---..', '----.'
         )

MORSE_CODE = dict(zip(symbols, codes))


def convert_string_to_morse_code(text: str) -> str:
    """
    Преобразует переданную строку в последовательность точек и тире,
    вставляя пробелы между отдельными словами.

    Символы, которые не находятся в словаре MORSE_CODE будут игнорироваться.
    """
    morse_string = ''

    for symbol in text.upper():
        if symbol not in MORSE_CODE.keys():
            continue
        else:
            morse_string += MORSE_CODE[symbol] + ' '

    return morse_string


def show_morse_code(text: str) -> None:
    """Выводит строку, преобразованную с помощью азбуки Морзе."""
    print(convert_string_to_morse_code(text))


def main():
    text = input("Введите строку: ")
    show_morse_code(text)


if __name__ == '__main__':
    main()
