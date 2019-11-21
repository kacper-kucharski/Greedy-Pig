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
    while True:
        game.changeTurn = False
        leaderBoard(True)
        while game.changeTurn == False:
            randomNumber()


def createPlayers(amountOfPlayers):
        allPlayers.append(classes.Player(input('Enter the name of player 1: '), True))

        for i in range(amountOfPlayers-1):
            allPlayers.append(classes.Player(input('Enter the name of player ' + str(i+2) + ' : '), False))

def leaderBoard(FirstTimeCalled):
    def totalSavedScoresList():
        print('\n*******************************')
        print('Total Saved Scores\n')
        for i in allPlayers:
            print(i.name + ' = ' + str(i.savedPoints))
        print('----------------------')
    totalSavedScoresList()
    for i in allPlayers:
        if i.hasTurn == True and game.changeTurn == False:
            game.currentPlayer = i
            print('Current Player:', game.currentPlayer.name)
            print('Your current score at this turn:', str(game.currentPlayer.currentPoints), '\n')
            if FirstTimeCalled == True:
                print(i.name + ' your first dice at this turn will be automatically rolled!\n')
                print('Ready?\n\n')
                input('press enter to continue ...')
            else:
                rollTurn = "r"
                passTurn = "p"
                input('press enter to continue ...')

                correctInput = False
                while correctInput == False:
                    rollOrPass = input('\n' + game.currentPlayer.name + ' choose your next decision: ' + rollTurn + ': roll the dice ' + passTurn + ': pass the turn and save your score: ') 
                    if rollOrPass == passTurn and game.currentPlayer.currentPoints + game.currentPlayer.savedPoints >= game.MaxPoint:
                        game.currentPlayer.savedPoints = game.currentPlayer.savedPoints + game.currentPlayer.currentPoints
                        totalSavedScoresList()
                        print('\n  ' + game.currentPlayer.name + ' won the game with a score of ' + game.currentPlayer.savedPoints + '\n')
                        exit()
                    elif rollOrPass == passTurn:
                        for e in range(len(allPlayers)):
                            if allPlayers[e].hasTurn == True:
                                try:
                                    game.currentPlayer = allPlayers[e+1]
                                except:
                                    game.currentPlayer = allPlayers[0]
                                game.currentPlayer.hasTurn = True
                                for o in allPlayers:
                                    if o.hasTurn and o != game.currentPlayer:
                                        o.hasTurn = not(o.hasTurn)
                                        o.savedPoints = o.savedPoints + o.currentPoints
                                        o.currentPoints = 0
                                print('Pass the dice to ' + game.currentPlayer.name)
                                game.changeTurn = True
                                correctInput = True
                                break
                    elif rollOrPass == rollTurn:
                        correctInput = True
                    else:
                        print("Invalid Input.")
            

def randomNumber():
    print('\n\n***********************')

    # Rethink design of the random number

    game.currentPlayer.turnPoints = random.randint(1,6)

    print('******** Rolled ' + str(game.currentPlayer.turnPoints) + ' *********')
    print('***********************')
    if game.currentPlayer.turnPoints == 1:
        game.currentPlayer.currentPoints = 0
        print('Oops! You lose ' + str(game.currentPlayer.turnPoints) + ' but still keep your previous '+ str(game.currentPlayer.savedPoints))

        for e in range(len(allPlayers)):
            if allPlayers[e].hasTurn == True:
                try:
                    game.currentPlayer = allPlayers[e+1]
                except:
                    game.currentPlayer = allPlayers[0]
                game.currentPlayer.hasTurn = True
                for o in allPlayers:
                    if o.hasTurn and o != game.currentPlayer:
                        o.hasTurn = not(o.hasTurn)
                        o.savedPoints = o.savedPoints + o.currentPoints
                        o.currentPoints = 0
                game.changeTurn = True
                break
    else:
        print('new collected score = ' + str(game.currentPlayer.currentPoints) + ' + ' + str(game.currentPlayer.turnPoints) +
         ' = ' + str(game.currentPlayer.currentPoints + game.currentPlayer.turnPoints) + '\n')
        game.currentPlayer.currentPoints = game.currentPlayer.currentPoints + game.currentPlayer.turnPoints
        leaderBoard(False)