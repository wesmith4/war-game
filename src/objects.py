from collections import deque
from random import shuffle


class Card:
    def __init__(self, value: str):
        self.value = value


class Deck:
    def __init__(self):
        values = [
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
        ]
        self.cards = deque([Card(value) for value in values * 4])

    def shuffle(self):
        shuffle(self.cards)

    def get_length(self):
        return self.cards.__len__()

    def take_one(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = deque()

    def get_length(self):
        return self.cards.__len__()

    def draw(self):
        return self.cards.pop()

    def pick_up(self, card: Card):
        self.cards.appendleft(card)


class Game:
    def __init__(self):
        self.deck = Deck()
        self.hand1 = Hand()
        self.hand2 = Hand()

    def deal(self):
        self.deck.shuffle()

        hand1 = True
        while self.deck.get_length() > 0:
            card = self.deck.take_one()

            if hand1:
                self.hand1.pick_up(card)
            else:
                self.hand2.pick_up(card)

            hand1 = not hand1

        print("Finished dealing")
