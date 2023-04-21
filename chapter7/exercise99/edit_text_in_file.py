def read_file(filename: str) -> str:
    """Считывает содержимое файла."""
    with open(filename, 'r') as file:
        return file.read()


def write_file(filename: str, data: str) -> None:
    """Записывает данные в файл."""
    with open(filename, 'w') as file:
        file.write(data)


def replace_keywords(text: str, keywords: list[str]) -> str:
    """Заменяет служебные слова на звездочки."""
    for word in text.split():
        if word.lower() in keywords:
            # Заменяем служебное слово в тексте на такое же слово в нижнем регистре.
            text = text.replace(word, word.lower())

    for keyword in keywords:
        text = text.replace(keyword, '*' * len(keyword))
    return text


def process_file(input_file: str, keywords_file: str, output_file: str) -> None:
    """Обрабатывает файл."""
    # Читаем список служебных слов.
    keywords = read_file(keywords_file).split()

    # Читаем исходный файл.
    text = read_file(input_file)

    # Заменяем служебные слова на звездочки.
    edited_text = replace_keywords(text, keywords)

    # Сохраняем отредактированный текст в новый файл.
    write_file(output_file, edited_text)

    print(f"\nФайл {input_file} успешно обработан.")


def main():
    path = 'files/'

    input_file = path + input("Введите имя исходного файла: ")
    keywords_file = path + input("Введите имя файла со служебными словами: ")
    output_file = path + input("Введите имя выходного файла: ")

    process_file(input_file, keywords_file, output_file)


if __name__ == '__main__':
    main()
