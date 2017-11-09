import sys

from card.Deck import Deck
from game.Hand import Hand
from game.order import get_best_hand


def distribute(deck, nb_of_players):
	players = [Hand("player"+str(i+1)) for i in range(nb_of_players)]
	for a in range(2):
		deck.throw_card()
		for b in range(nb_of_players):
			players[b].add_card(deck.pick_card())

	return players


def get_river(deck):
	river = Hand("river")
	deck.throw_card()
	river.add_card(deck.pick_card())
	river.add_card(deck.pick_card())
	river.add_card(deck.pick_card())
	deck.throw_card()
	river.add_card(deck.pick_card())
	deck.throw_card()
	river.add_card(deck.pick_card())
	return river


def main():
	print(sys.version)
	deck = Deck().shuffle()

	players = distribute(deck, 2)
	river = get_river(deck)

	winner = get_best_hand(river, players)


if __name__ == "__main__":
	main()
