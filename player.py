class Player:
    def __init__(self, name, symbol = 0, turn = 0, won = 0):
        self.name = name
        self.symbol = symbol
        self.turn = turn
        self.won = won

    def setName(self, name):
        self.name = name
    def setSymbol(self, symbol):
        self.symbol = symbol
    def setTurn(self, turn):
        self.turn = turn
    def setWon(self, won):
        self.won = won
    def getName(self):
        return self.name
    def getSymbol(self):
        return self.symbol
    def getTurn(self):
        return self.turn
    def getWon(self):
        return self.won

    def win(self):
        print("Ganador", self.name)

    def looser(self):
        print("Perdedor", self.name)

    def getPlayer(self):
        print(self.name)
        print(self.symbol)
        print(self.turn)
        print(self.won)

