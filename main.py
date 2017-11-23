import sys

from card.Card import Card
from card.Deck import Deck
from game.Hand import Hand
from game.order import getbesthand


def distribute(deck, numberofplayers):
	players = [Hand("player"+str(i+1)) for i in range(numberofplayers)]
	for a in range(2):
		deck.throw_card()
		for b in range(numberofplayers):
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

	players = distribute(deck, 4)
	river = get_river(deck)

	winner = getbesthand(river, players)
	if winner is None:
		print("Equality !")
	else:
		print("The winner hand")
		print([(card.color, card.value) for card in winner])


def test():
	player_1 = Hand("Player1")
	player_1.add_card(Card('Heart', 'As', 14))
	player_1.add_card(Card('Heart', 'King', 13))
	player_2 = Hand("Player2")
	player_2.add_card(Card('Diamond', '5', 5))
	player_2.add_card(Card('Diamond', '6', 6))
	players = [player_1, player_2]
	river = Hand("River")
	river.add_card(Card('Heart', 'Queen', 12))
	river.add_card(Card('Heart', 'Jack', 11))
	river.add_card(Card('Heart', '10', 10))
	river.add_card(Card('Heart', '9', 9))
	river.add_card(Card('Heart', '8', 8))

	winner = getbesthand(river, players)
	if winner is None:
		print("Equality !")
	else:
		print("The winner hand")
		print([(card.color, card.value) for card in winner])


if __name__ == "__main__":
	main()
	# test()
