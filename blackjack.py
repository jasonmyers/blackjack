class Hand(object):
	card_values = {
				    "ace" : 11, "king" : 10, "queen" : 10, "jack" : 10,
				    "ten" : 10, "nine" : 9, "eight" : 8, "seven" : 7,
				    "six" : 6, "five" : 5, "four" : 4, "three" : 3,	
				    "two" : 2
			      }
	def __init__(self):
		self.cards = []

	def add_card(self, card):
		self.cards.append(card.__repr__())

	def calculate_hand_score(self):
		hand_total = 0
		for card in self.cards:
			hand_total += self.card_values[card[0]]
		return hand_total

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


def get_winning_hand(hand1, hand2):
	if hand1.calculate_hand_score() == hand2.calculate_hand_score():
		return "draw"
	elif hand1.calculate_hand_score() > hand2.calculate_hand_score():
		return hand1
	else:
		return hand2













