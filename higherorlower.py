import cardlib

class HigherOrLower:
	def __init__(self):
		self.deck = cardlib.Deck()
		self.score = 0
		
	def start(self):
		self.deck.shuffle()
		
		self.topCard = self.deck.pop()
		
		print(self.topCard.toString())
		
		return self.topCard
	
	def giveMove(self, move):
		if move != "higher" and move != "lower":
			print ("Error: Bad input, Expected higher or lower")
			print(self.topCard.toString())
			return
	
		previousCard = self.topCard
		self.topCard = self.deck.pop()
		
		compareValue = self.topCard.compare(previousCard)
		
		if move == "higher":
			if compareValue == 1: self.score += 1
			elif compareValue == -1: self.score -= 1
		elif move == "lower":
			if compareValue == 1: self.score -= 1
			elif compareValue == -1: self.score += 1
	
		
		print(self.topCard.toString())
		print("Score:")
		print(self.score)
		
		return self.topCard
	
	