from random import randrange


def create_deck() -> list:
    """Создаёт колоду из 52 карт."""
    nominal = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suits = ['s', 'h', 'd', 'c']
    deck = []

    for i in suits:
        for j in nominal:
            deck.append(f"{j}{i}")

    return deck


def shuffle(deck: list) -> list:
    """Тасует колоду карт."""
    number_cards = len(deck)

    for i in range(number_cards):
        j = randrange(i, number_cards)
        deck[i], deck[j] = deck[j], deck[i]

    return deck


def show_deck(deck: list) -> None:
    """Выводит колоду карт."""
    print(deck)


def main():
    deck = create_deck()

    print("\nКолода карт до тасования:")
    show_deck(deck)

    shuffled_deck = shuffle(deck)

    print("\nКолода карт после тасования:")
    show_deck(shuffled_deck)


if __name__ == '__main__':
    main()
