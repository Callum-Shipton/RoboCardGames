import higherorlower

game = higherorlower.HigherOrLower()

game.start()

for i in range(10):
	input = raw_input('Higher or Lower?: ')
	game.giveMove(input)