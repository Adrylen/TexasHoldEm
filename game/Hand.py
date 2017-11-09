class Hand:
	def __init__(self, name):
		self.name = name
		self.cards = []

	def add_card(self, card):
		self.cards.append(card)

	def __str__(self):
		return self.name + " : " + "".join([str(card) + " | " for card in self.cards])
