class Player:
    def __init__(self, name, hasTurn, currentPoints = 0, savedPoints = 0):
        self.name = name
        self.currentPoints = currentPoints
        self.savedPoints = savedPoints
        self.hasTurn = hasTurn
    
    def GetName(self):
        return self.name

class Game:
    def __init__(self, gameMode, amountOfPlayers):
        self.__gameMode = gameMode
        self.amountOfPlayers = amountOfPlayers
        self.setMaxPoint(gameMode)
        self.currentPlayer = None
    
    def setMaxPoint(self, gameMode):
        if self.__gameMode == 1:
            return 50
        else:
            return 100