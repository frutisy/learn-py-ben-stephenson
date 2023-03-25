from chapter5.exercise77.shuffle_deck_of_cards import create_deck
from chapter5.exercise77.shuffle_deck_of_cards import shuffle


def verify_number_of_players(players: int) -> None:
    """Проверяет количество введённых игроков."""
    if players < 2:
        raise ValueError("Количество игроков должно быть как минимум 2")


def verify_number_of_cards_per_player(cards_per_player: int) -> None:
    """Проверяет количество введённых карт на одного игрока."""
    if cards_per_player < 2:
        raise ValueError(
            "Количество раздаваемых карт должно быть как минимум 2")


def verify_number_of_cards_handout(players: int, cards_per_player: int, deck: list) -> None:
    """Проверяет сумму розданных карт всех игроков."""
    length_of_deck = len(deck)

    if players * cards_per_player > length_of_deck:
        raise ValueError(
            f"Количество раздаваемых карт не может быть больше {length_of_deck}")


def deal(players: int = 2, cards_per_player: int = 2, deck=None) -> list:
    if deck is None:
        deck = create_deck()

    verify_number_of_players(players)
    verify_number_of_cards_per_player(cards_per_player)
    verify_number_of_cards_handout(players, cards_per_player, deck)

    hands = [[] for i in range(players)]

    for i in range(cards_per_player):
        for j in range(players):
            hands[j].append(deck[0])
            deck.pop(0)

    return hands


def main():
    deck = create_deck()
    shuffled_deck = shuffle(deck)

    players = 4
    cards_per_player = 5

    print(f"Играют {players} игрока. Каждый имеет по {cards_per_player} карт\n")
    print(f"Карманные карты всех игроков:\n{deal(players, cards_per_player, shuffled_deck)}\n")
    print(f"Оставшиеся карты:\n{shuffled_deck}")


if __name__ == '__main__':
    main()
