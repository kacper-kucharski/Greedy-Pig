import classes, random


allPlayers = []



def welcomeScreen():
    print('*******************************')
    print('Welcome to GAME OF PIG')
    print('*******************************')
    print('To start the game, please set up the game: \n')

def gameModeInputCheck():    
    correctInput = False
    while correctInput != True:
        gameMode = input("please choose the mode of the game: '1': Beginners   '2': Advanced --- ")
        if gameMode == '1' or gameMode == '2':
            correctInput = True
            return gameMode

def playerAmountInputCheck():
    correctInput = False
    while correctInput != True:
        playerAmount = int(input('please enter the number of players (2-6): '))
        if playerAmount >= 2 and playerAmount <= 6:
            correctInput = True
            return playerAmount

def Start():
    global game
    welcomeScreen()
    game = classes.Game(gameModeInputCheck(), playerAmountInputCheck())
    createPlayers(game.amountOfPlayers)
              
    leaderBoard()
    randomNumber()


def createPlayers(amountOfPlayers):
        allPlayers.append(classes.Player(input('Enter the name of player 1: '), True))

        for i in range(amountOfPlayers-1):
            allPlayers.append(classes.Player(input('Enter the name of player ' + str(i+2) + ' : '), False))

def leaderBoard():
    print('\n*******************************')
    print('Total Saved Scores\n')
    for i in allPlayers:
        print(i.name + ' = ' + str(i.savedPoints))
    print('----------------------')
    for i in allPlayers:
        if i.hasTurn == True:
            game.currentPlayer = i
            print('Current Player:', game.currentPlayer.name)
            print('Your current score at this turn:', str(game.currentPlayer.currentPoints), '\n')
            print(i.name + ' your first dice at this turn will be automatically rolled!\n')
            print('Ready?\n\n')
            input('press enter to continue ...')

def randomNumber():
    print('\n\n***********************')

    # Rethink design of the random number
    game.currentPlayer.currentPoints = random.randint(0,6)

    print('******** Rolled ' + str(game.currentPlayer.currentPoints) + ' *********')
    print('***********************')
    print('new collected score = ' + str(game.currentPlayer.savedPoints) + ' + ' + str(game.currentPlayer.currentPoints) +
         ' = ' + str(game.currentPlayer.savedPoints + game.currentPlayer.currentPoints) + '\n')

