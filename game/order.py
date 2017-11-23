from itertools import groupby
import sys


def getweight(hand):
	return sum([card.weight for card in hand])


def combination(bighand, hand, length):
	grouped = [list(group) for key, group in groupby(sorted(card.weight for card in bighand))]
	square = [g for g in grouped if len(g) == length]
	if not square:
		return False
	for card in bighand:
		if card.weight == square[0][0]:
			hand.append(card)
	return True


def isquinteflushroyal(bighand, hand):
	if isquinteflush(bighand, hand):
		return hand[0].value == 'As'
	return False


def isquinteflush(bighand, hand):
	tmphand = []
	if iscolor(bighand, tmphand) and isquinte(tmphand, hand):
		return True
	return False


def issquare(bighand, hand):
	return combination(bighand, hand, 4)


def isfull(bighand, hand):
	brelan = []
	if not isbrelan(bighand, brelan):
		return False
	rest = [card for card in bighand if card not in brelan]
	pair = []
	if not ispair(rest, pair):
		return False
	rest = [card for card in rest if card not in pair]
	otherpair = []
	if ispair(rest, otherpair):
		pair = pair if getweight(pair) > getweight(otherpair) else otherpair

	hand.extend(brelan + pair)
	return True


def iscolor(bighand, hand):
	grouped = [list(group) for key, group in groupby(sorted(card.color for card in bighand))]
	color = [g for g in grouped if len(g) >= 5]
	if not color:
		return False
	for card in bighand:
		if card.color == color[0][0]:
			hand.append(card)
	return True


def isquinte(bighand, hand):
	sort = sorted([card.weight for card in bighand], reverse=True)
	quinte = []
	previous = -1
	for value in sort:
		if previous != -1:
			if value == previous - 1:
				quinte.append(value)
				if len(quinte) == 5:
					break
			else:
				quinte = []
		else:
			quinte.append(value)
		previous = value
	if len(quinte) < 5:
		return False
	for weight in quinte:
		for card in bighand:
			if weight == card.weight:
				hand.append(card)
				break
	return True


def isbrelan(bighand, hand):
	return combination(bighand, hand, 3)


def isdoublepair(bighand, hand):
	first = []
	if not ispair(bighand, first):
		return False
	rest = [card for card in bighand if card not in first]
	second = []
	if not ispair(rest, second):
		return False
	if getweight(first) > getweight(second):
		hand.extend(first + second)
	else:
		hand.extend(second + first)
	return True


def ispair(bighand, hand):
	return combination(bighand, hand, 2)


def completehand(bighand, hand):
	rest = [card for card in bighand if card not in hand]
	while len(hand) < 5:
		maxcard = None
		for card in rest:
			if maxcard is None:
				maxcard = card
			elif card.weight > maxcard.weight:
				maxcard = card
		rest.remove(maxcard)
		hand.append(maxcard)


def getwinner(players):
	handstate = max(p[1] for p in players)
	potential = [p[0] for p in players if p[1] == handstate]
	for i in range(5):
		maxplayer = None
		equal = False
		for p in potential:
			if maxplayer is None:
				maxplayer = p
			elif maxplayer[i].weight < p[i].weight:
				maxplayer = p
			elif maxplayer[i].weight == p[i].weight:
				equal = True
		if equal:
			continue
		else:
			return maxplayer
	return None


def getbesthand(river, hands):
	players = []
	for h in hands:
		bighand = river.cards + h.cards
		hand = []

		if isquinteflushroyal(bighand, hand):
			value = 9
			print('Quinte Flush Royal')
		elif isquinteflush(bighand, hand):
			value = 8
			print('Quinte Flush')
		elif issquare(bighand, hand):
			value = 7
			print('Square')
		elif isfull(bighand, hand):
			value = 6
			print('Full')
		elif iscolor(bighand, hand):
			value = 5
			print('Color')
		elif isquinte(bighand, hand):
			value = 4
			print('Quinte')
		elif isbrelan(bighand, hand):
			value = 3
			print('Brelan')
		elif isdoublepair(bighand, hand):
			value = 2
			print('Double pair')
		elif ispair(bighand, hand):
			value = 1
			print('Pair')
		else:
			value = 0
			print('Highest card')

		if len(hand) < 5:
			completehand(bighand, hand)

		players.append((hand, value))
		print([(card.color, card.value) for card in hand])

	return getwinner(players)


def main():
	print(sys.version)


if __name__ == "__main__":
	main()
