class Card:
	def __init__(self, number, suit):
		self.number = number
		self.suit = suit
		self.value = number
		
		if number == 'Ace': self.value = 1
		elif number == 'Jack': self.value = 11
		elif number == 'Queen': self.value = 12
		elif number == 'King': self.value = 13
	
	def compare(self, card):
		if self.value > card.value: return 1
		if self.value < card.value: return -1
		return 0
		
	def toString(self):
		return self.number + " of " + self.suit + "s"
	
class Deck:
	def __init__(self):
		self.cards = [Card('Ace', 'Spade'), Card('2', 'Spade'), Card('3', 'Spade'), Card('4', 'Spade'), Card('5', 'Spade'), Card('6', 'Spade'), Card('7', 'Spade'), Card('8', 'Spade'), Card('9', 'Spade'), Card('10', 'Spade'), Card('Jack', 'Spade'), Card('Queen', 'Spade'), Card('King', 'Spade'), Card('Ace', 'Diamond'), Card('2', 'Diamond'), Card('3', 'Diamond'), Card('4', 'Diamond'), Card('5', 'Diamond'), Card('6', 'Diamond'), Card('7', 'Diamond'), Card('8', 'Diamond'), Card('9', 'Diamond'), Card('10', 'Diamond'), Card('Jack', 'Diamond'), Card('Queen', 'Diamond'), Card('King', 'Diamond'), Card('Ace', 'Club'), Card('2', 'Club'), Card('3', 'Club'), Card('4', 'Club'), Card('5', 'Club'), Card('6', 'Club'), Card('7', 'Club'), Card('8', 'Club'), Card('9', 'Club'), Card('10', 'Club'), Card('Jack', 'Club'), Card('Queen', 'Club'), Card('King', 'Club'), Card('Ace', 'Heart'), Card('2', 'Heart'), Card('3', 'Heart'), Card('4', 'Heart'), Card('5', 'Heart'), Card('6', 'Heart'), Card('7', 'Heart'), Card('8', 'Heart'), Card('9', 'Heart'), Card('10', 'Heart'), Card('Jack', 'Heart'), Card('Queen', 'Heart'), Card('King', 'Heart')]
	
	def shuffle(self):
		print("Shuffling")
		
	def pop(self):
		return self.cards.pop(0)