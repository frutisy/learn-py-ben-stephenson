def is_ie_correct(word: str) -> bool:
    """
    Проверяет, соответствует ли написание анализируемого слова правилу
    «I before E except after C» (I перед E, если не после C).

    Возвращает True, если написание слова соответствует правилу, иначе - False.
    """
    if 'ei' in word:
        if 'cei' in word:
            return True
        elif 'ie' in word:
            return False
        else:
            return True
    elif 'ie' in word:
        if 'cie' in word:
            return False
        else:
            return True
    else:
        return False


def get_correct_incorrect_words(file_path: str) -> tuple[set[str], set[str]]:
    """
    Обрабатывает текстовый файл и возвращает два списка: слова, которые
    следуют правилу "I before E except after C" и слова, которые не следуют
    данному правилу.

    Возвращает кортеж из двух списков: корректные слова и некорректные слова.
    """
    correct_words = []
    incorrect_words = []

    with open(file_path, 'r') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                if 'ei' in word or 'ie' in word:
                    if is_ie_correct(word):
                        if word not in correct_words:
                            correct_words.append(word)
                    else:
                        if word not in incorrect_words:
                            incorrect_words.append(word)

    return set(correct_words), set(incorrect_words)


def show_results(correct_words, incorrect_words) -> None:
    """
    Выводит на экран два списка: корректные слова и некорректные слова,
    а также количество слов в каждом списке.
    """
    print("Слова, соответствующие правилу:", ", ".join(correct_words))
    print("Количество слов, соответствующих правилу:", len(correct_words))
    print("Слова, нарушающие правило:", ", ".join(incorrect_words))
    print("Количество слов, нарушающих правило:", len(incorrect_words))


def main():
    file_path = 'files/words.txt'
    correct_words, incorrect_words = get_correct_incorrect_words(file_path)
    show_results(correct_words, incorrect_words)


if __name__ == '__main__':
    main()
