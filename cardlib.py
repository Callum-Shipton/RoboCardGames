import random
import itertools

class Card:
	def __init__(self, number, suit):
		self.number = number
		self.suit = suit
		self.value = number
		
		if number == 'Ace': self.value = 1
		elif number == 'Jack': self.value = 11
		elif number == 'Queen': self.value = 12
		elif number == 'King': self.value = 13
		else: self.value = int(number)
	
	def compare(self, card):
		if self.value > card.value: return 1
		if self.value < card.value: return -1
		return 0
		
	def toString(self):
		return self.number + " of " + self.suit + "s"
	
class Deck:
	cards = []
	def __init__(self):
		values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
		suits = ['Spade', 'Diamond', 'Club', 'Heart']
		allCards = itertools.product(values, suits)
		for number,suit in allCards:
			self.cards.append(Card(number, suit))
	
	def shuffle(self):
		print("Shuffling")
		random.seed(31415)
		random.shuffle(self.cards)
		
	def pop(self):
		return self.cards.pop(0)