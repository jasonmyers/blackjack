class Hand(object):
	def __init__(self):
		self.cards = []

	def addCard(self, card):
		self.cards.append(card.__repr__())

class Card(object):
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __repr__(self):
		return (self.rank, self.suit)

class Dealer(Hand):
	def print_hand(self):
		return 'XX' + ' & ' + ' & '.join([card[0] + ' of ' + card[1] for card in self.cards[1:]])

class Player(Hand):
	def print_hand(self):
		return ' & '.join([card[0] + ' of ' + card[1] for card in self.cards])