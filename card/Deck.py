from card import Card as cd
import random

class Deck:


    def __init__(self):
        self.colors=['Spade','Heart','Diammond','Clover']
        self.values=['2','3','4','5','6','7','8','9','10','Jack','Queen','King','As']
        self.cards=[]

        for color in self.colors:
            for value in self.values:
                self.cards.append(cd.Card(color,value,self.values.index(value)+2))


    def __str__(self):
        tostr = ''
        for card in self.cards:
            tostr +=  card + '\n'
        return (tostr)

    def shuffle(self):
        random.shuffle(self.cards)
