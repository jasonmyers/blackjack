import unittest
from blackjack import Hand, Card, Dealer, Player, get_winning_hand

class BlackjackTest(unittest.TestCase):
	def setUp(self):
		deck = ["ace,spades", "king,spades", "queen,spades", "jack,spades", "ten,spades",
		"nine,spades", "eight,spades", "seven,spades", "six,spades", 
		"five,spades", "four,spades", "three,spades", "two,spades",
		"ace,clubs", "king,clubs", "queen,clubs", "jack,clubs", "ten,clubs",
		"nine,clubs", "eight,clubs", "seven,clubs", "six,clubs", 
		"five,clubs", "four,clubs", "three,clubs", "two,clubs",
		"ace,hearts", "king,hearts", "queen,hearts", "jack,hearts", "ten,hearts",
		"nine,hearts", "eight,hearts", "seven,hearts", "six,hearts", 
		"five,hearts", "four,hearts", "three,hearts", "two,hearts",
		"ace,diamonds", "king,diamonds", "queen,diamonds", "jack,diamonds", "ten,diamonds",
		"nine,diamonds", "eight,diamonds", "seven,diamonds", "six,diamonds", 
		"five,diamonds", "four,diamonds", "three,diamonds", "two,diamonds"
       ]

	def create_card_test(self):
		c1 = Card("ten","clubs")
		self.assertEqual(("ten","clubs"), c1.__repr__())

	def create_hand_test(self):
		set1 = Hand()
		set1.add_card(Card("ace","spades"))
		set1.add_card(Card("king","spades"))
		self.assertEqual([("ace","spades"),("king","spades")], set1.cards)

	def create_player_test(self):
		p1 = Player()
		p1.add_card(Card("ace","spades"))
		p1.add_card(Card("jack","hearts"))

		self.assertEqual([("ace","spades"),("jack","hearts")], p1.cards)

	def check_hands_test(self):
		p1 = Player()
		p1.add_card(Card("ace","spades"))
		p1.add_card(Card("jack","hearts"))

		self.assertEqual("ace of spades & jack of hearts", p1.print_hand())

		p2 = Dealer()
		p2.add_card(Card("one","spades"))
		p2.add_card(Card("ten","diamonds"))

		self.assertEqual("XX & ten of diamonds", p2.print_hand())

	def get_hand_score_test(self):
		p1 = Player()
		p1.add_card(Card("ace","spades"))
		p1.add_card(Card("jack","hearts"))		
		self.assertEqual(21, p1.calculate_hand_score())

	def check_hands_for_winning_hand_test(self):
		p1 = Player()
		p1.add_card(Card("ace","spades"))
		p1.add_card(Card("jack","hearts"))

		p2 = Player()
		p2.add_card(Card("ace","spades"))
		p2.add_card(Card("nine","hearts"))		

		self.assertEqual(p1, get_winning_hand(p1,p2))

		p3 = Player()
		p3.add_card(Card("ace","diamonds"))
		p3.add_card(Card("jack","clubs"))
		self.assertEqual("draw", get_winning_hand(p1,p3))
