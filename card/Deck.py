from card.Card import Card
import random


class Deck:
    def __init__(self):
        self.colors = ['Spade', 'Heart', 'Diamond', 'Clover']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'As']
        self.cards = []
        self.rank = -1

        for color in self.colors:
            for value in self.values:
                self.cards.append(Card(color, value, self.values.index(value)+2))

    def __str__(self):
        return "".join([str(card) + "\n" for card in self.cards])

    def throw_card(self):
        self.rank += 1

    def pick_card(self):
        self.rank += 1
        return self.cards[self.rank]

    def shuffle(self):
        random.shuffle(self.cards)
        return self
