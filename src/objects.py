from collections import deque
from random import shuffle
import pandas as pd

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

    def pick_up_cards(self, cards: deque):
        self.cards.extendleft(cards)


class Player:
    def __init__(self, name: str, hand: Hand):
        self.name = name
        self.hand = hand


class Game:
    def __init__(self, player1Name, player2Name):
        self.deck = Deck()
        self.player1 = Player(player1Name, Hand())
        self.player2 = Player(player2Name, Hand())
        self.turn = 0
        self.history = []

    def shuffle_and_deal(self):
        self.deck.shuffle()

        hand1 = True
        while self.deck.get_length() > 0:
            card = self.deck.take_one()

            if hand1:
                self.player1.hand.pick_up_cards(deque([card]))
            else:
                self.player2.hand.pick_up_cards(deque([card]))

            hand1 = not hand1

        self.history.append(
            {
                "Turn": self.turn,
                "P1": self.player1.hand.get_length(),
                "P2": self.player2.hand.get_length(),
            }
        )

    def playTurn(self):
        self.turn += 1

        stack = deque()
        card1 = self.player1.hand.draw()
        card2 = self.player2.hand.draw()

        if card1.value == card2.value:
            if self.player1.hand.get_length() < 2:
                stack.appendleft(card1)
                stack.appendleft(card2)
                self.player2.hand.pick_up_cards(stack)
            elif self.player2.hand.get_length() < 2:
                stack.appendleft(card1)
                stack.appendleft(card2)
                self.player1.hand.pick_up_cards(stack)

            while card1.value == card2.value:
                stack.appendleft(card1)
                stack.appendleft(card2)
                stack.appendleft(self.player1.hand.draw())
                stack.appendleft(self.player2.hand.draw())

                card1 = self.player1.hand.draw()
                card2 = self.player2.hand.draw()

        stack.appendleft(card1)
        stack.appendleft(card2)

        if ranks[card1.value] > ranks[card2.value]:
            self.player1.hand.pick_up_cards(stack)
        else:
            self.player2.hand.pick_up_cards(stack)

        self.history.append(
            {
                "Turn": self.turn,
                "P1": self.player1.hand.get_length(),
                "P2": self.player2.hand.get_length(),
            }
        )

    def in_progress(self):
        return (
            self.player1.hand.get_length() > 0
            and self.player2.hand.get_length() > 0
        )

    def get_results(self):
        if self.player1.hand.get_length() == 52:
            winner = self.player1
        elif self.player2.hand.get_length() == 52:
            winner = self.player2
        else:
            raise Exception("Game still in progress")

        return {
            "Winner": winner,
            "Turns": self.turn,
            "Results": pd.DataFrame(self.history),
        }

    def play(self):
        self.shuffle_and_deal()
        print(
            "%s : %s cards"
            % (self.player1.name, self.player1.hand.get_length())
        )
        print(
            "%s : %s cards"
            % (self.player2.name, self.player2.hand.get_length())
        )
        while self.in_progress():
            self.playTurn()
            print(
                "%s : %s cards"
                % (self.player1.name, self.player1.hand.get_length())
            )
            print(
                "%s : %s cards"
                % (self.player2.name, self.player2.hand.get_length())
            )

        return self.get_results()
