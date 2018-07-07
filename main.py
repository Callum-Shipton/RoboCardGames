import higherorlower
import kerasnn_01

numberOfGames = 140

ai = kerasnn_01.KerasNN()

for runId in range(0, numberOfGames):
    game = higherorlower.HigherOrLower()

    state = game.start()

    for card in range(1,51):
        input = ai.getMove(state)
        print(input)
        response = game.giveMove(input)
        state = response.gameState
        ai.storeResponse(response.success)
    print("Score: ")
    print(game.score)

    ai.train()