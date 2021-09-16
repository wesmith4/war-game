from collections import deque
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


def playTurn(game: Game):
    stack = deque()
    card1 = game.hand1.draw()
    card2 = game.hand2.draw()

    if card1.value == card2.value:
        while card1.value == card2.value:
            stack.appendleft(card1)
            stack.appendleft(card2)
            stack.appendleft(game.hand1.draw())
            stack.appendleft(game.hand2.draw())

            card1 = game.hand1.draw()
            card2 = game.hand2.draw()

    stack.appendleft(card1)
    stack.appendleft(card2)

    if card1Higher(card1, card2):
        game.hand1.pick_up_cards(stack)
    else:
        game.hand2.pick_up_cards(stack)


def card1Higher(card1: Card, card2: Card):
    """Returns True or False"""
    return ranks[card1.value] > ranks[card2.value]


game = Game()
game.deal()


for i in range(20):
    playTurn(game)

print(game.hand1.cards.__len__())
