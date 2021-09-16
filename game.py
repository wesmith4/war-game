from src.objects import Game, Deck, Hand, Card

ranks = {
    "A": 13,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "10": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
}

game = Game()

game.deal()


def compare(card1: Card, card2: Card):

    if ranks[card1.value] == ranks[card2.value]:
        return "Tie"
    card1_wins = ranks[card1.value] > ranks[card2.value]
