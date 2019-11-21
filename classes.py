class Player:
    def __init__(self, name, hasTurn, currentPoints = 0, savedPoints = 0):
        self.name = name
        self.currentPoints = currentPoints
        self.savedPoints = savedPoints
        self.turnPoints = 0
        self.hasTurn = hasTurn

class Game:
    def __init__(self, gameMode, amountOfPlayers):
        self.__gameMode = int(gameMode)
        self.amountOfPlayers = amountOfPlayers
        self.MaxPoint = self.setMaxPoint(self.__gameMode)
        self.currentPlayer = None
        self.currentPlayerNumber = 0
        self.changeTurn = False
    
    def setMaxPoint(self, gameMode):
        if self.__gameMode == 1:
            return 50
        else:
            return 100