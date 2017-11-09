from itertools import groupby
import sys


def get_quinte_flush(big_hand):
	grouped = [list(group) for key, group in groupby(sorted([card.color for card in big_hand]))]

# ====================
# 	print([c.weight for c in big_hand])
	# print(max(big_hand, key=lambda x: x.weight))
# ====================

	flush = [group for group in grouped if len(group) >= 5]
	if not flush:
		return None
	print(flush)

	# if 5 in [len(list(group)) for key, group in groupby(sorted([card.color for card in big_hand]))]:
	# 	temp = filter(lambda x: )
	return None


def get_best_hand(river, hands):
	weights = []
	for hand in hands:
		big_hand = river.cards + hand.cards

		sum = 0
		for card in big_hand:
			sum += card.weight
		weights.append(sum)

		# temp = get_quinte_flush(big_hand)

		# for h in big_hand:
		# 	print(h)
	print(weights)
	return None


def main():
	print(sys.version)


if __name__ == "__main__":
	main()
