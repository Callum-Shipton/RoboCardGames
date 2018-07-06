import cardlib

class Blackjack
	def __init__(self, players):
		self.deck = cardlib.Deck()
		self.deck.shuffle()
		self.hands = dict()
		for player in range(players):
			hand = List()
			hand.append(deck.pop())
			hand.append(deck.pop())
			self.hands[player](hand)
			
	def getHand(index):
		return self.hands[index]
		
	def twist(self, index):
		self.hands[index].append(self.deck.pop())
	
	def skip(self):	