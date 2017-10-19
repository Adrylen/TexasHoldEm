from game.Hand import Hand


class River(Hand):
	def __init__(self, name):
		super().__init__(name)

	def get_best_hand(self, hands):
		weights = []
		for hand in hands:
			weights.append(self.get_hand_weight(hand + self.cards))

	def get_hand_weight(self, cards):
		weight = sum([card.weight for card in cards])
		return weight
