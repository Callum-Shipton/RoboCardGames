import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.optimizers import RMSprop

import numpy as np

class KerasNN:

	x_train = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13]]
	x_trainNP = np.asarray(x_train)
	x_trainNorm = (x_trainNP-1)/12
	
	y_train = [[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]]
	y_trainNP = np.asarray(y_train)

	def __init__(self):
		self.lastMove = []
		self.trainingInput = []
		self.trainingResponses = []
	
		self.model = Sequential()
		self.model.add(LSTM(32, return_sequences=True, stateful=True, input_shape=(1,)))
		self.model.add(LSTM(32, return_sequences=True, stateful=True))
		self.model.add(LSTM(32, stateful=True))
		self.model.add(Dense(2, activation='softmax'))

		self.model.compile(loss='categorical_crossentropy',
			optimizer=RMSprop(),
			metrics=['accuracy'])

	def getMove(self, state):
		inputValue = state.value
		self.trainingInput.append((inputValue-1)/12)
		move = self.model.predict_classes(np.asarray([(inputValue-1)/12]))
		self.lastMove = move
		actualMove = move[0]
		if actualMove == 0:
			return "higher"
		else:
			return "lower"

	def storeResponse(self, success):
		if success == False: 
			if self.lastMove[0] == 0:
				self.trainingResponses.append([0, 1])
			else:
				self.trainingResponses.append([1, 0])
		else:
			if self.lastMove[0] == 0:
				self.trainingResponses.append([1, 0])
			else:
				self.trainingResponses.append([0, 1])

	def train(self):
		self.model.fit(np.asarray(self.trainingInput), np.asarray(self.trainingResponses),
						batch_size=52,
						epochs=10,
						verbose=1,
						validation_data=(self.x_trainNorm, self.y_trainNP))