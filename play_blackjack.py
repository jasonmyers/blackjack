from blackjack import Hand, Card, Dealer, Player, get_winning_hand
import random





if __name__ == '__main__':

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
	"five,diamonds", "four,diamonds", "three,diamonds", "two,diamonds"]
	
	play_game = True
	
	while play_game:
		print "---- Start of Round ----"
		print "dealing cards ...."
		dealer = Dealer()
		# Deal 2 cards for Dealer
		playing_card = random.choice(deck)
		print playing_card
		deck.remove(playing_card)
		rank, suit = playing_card.split(',')
		dealer.add_card(Card(rank,suit))
		playing_card = random.choice(deck)
		print playing_card
		deck.remove(playing_card)
		rank, suit = playing_card.split(',')
		dealer.add_card(Card(rank,suit))

		# Deal player cards
		player = Player()
		playing_card = random.choice(deck)
		deck.remove(playing_card)
		rank, suit = playing_card.split(',')
		player.add_card(Card(rank,suit))
		playing_card = random.choice(deck)
		deck.remove(playing_card)
		rank, suit = playing_card.split(',')
		player.add_card(Card(rank,suit))

		# Show hands
		print "Dealers Hand : %s", dealer.print_hand()
		print "Players Hand : %s", player.print_hand()

		# Get choice from Player
		player_choice = raw_input("Enter Choice : H(it) or S(tand) - ")
		if player_choice == 'H':
			playing_card = random.choice(deck)
			deck.remove(playing_card)
			rank, suit = playing_card.split(',')
			player.add_card(Card(rank,suit))

		print "Dealers Hand : %s", ' & '.join([card[0] + ' of ' + card[1] for card in dealer.cards])
		print "Players Hand : %s", player.print_hand()

		if (get_winning_hand(dealer,player) == player):
			print "Player Wins!!"
		else:
			print "Dealer Wins ...."	

		play_game = False
