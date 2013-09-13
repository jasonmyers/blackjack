import unittest
from blackjack import Hand, Card, Dealer, Player, get_winning_hand

class BlackjackTest(unittest.TestCase):
	def create_card_test(self):
		c1 = Card("ten","clubs")
		self.assertEqual(("ten","clubs"), c1.__repr__())

	def create_hand_test(self):
		set1 = Hand()
		set1.addCard(Card("ace","spade"))
		set1.addCard(Card("king","spade"))
		self.assertEqual([("ace","spade"),("king","spade")], set1.cards)

	def create_player_test(self):
		p1 = Player()
		p1.addCard(Card("ace","spade"))
		p1.addCard(Card("jack","hearts"))

		self.assertEqual([("ace","spade"),("jack","hearts")], p1.cards)

	def check_hands_test(self):
		p1 = Player()
		p1.addCard(Card("ace","spade"))
		p1.addCard(Card("jack","hearts"))

		self.assertEqual("ace of spade & jack of hearts", p1.print_hand())

		p2 = Dealer()
		p2.addCard(Card("one","spade"))
		p2.addCard(Card("ten","diamonds"))

		self.assertEqual("XX & ten of diamonds", p2.print_hand())

	def get_hand_score_test(self):
		p1 = Player()
		p1.addCard(Card("ace","spade"))
		p1.addCard(Card("jack","hearts"))		
		self.assertEqual(21, p1.calculate_hand_score())

	def check_hands_for_winning_hand_test(self):
		p1 = Player()
		p1.addCard(Card("ace","spade"))
		p1.addCard(Card("jack","hearts"))

		p2 = Player()
		p2.addCard(Card("ace","spade"))
		p2.addCard(Card("nine","hearts"))		

		self.assertEqual(p1, get_winning_hand(p1,p2))

		p3 = Player()
		p3.addCard(Card("ace","diamonds"))
		p3.addCard(Card("jack","clubs"))
		self.assertEqual("draw", get_winning_hand(p1,p3))
