#Clase Player
class Player:
    #Constructor de la clase
    def __init__(self, name, symbol = 0, turn = 0, won = 0):
        self.name = name
        self.symbol = symbol
        self.turn = turn
        self.won = won
    #metodo para setear el nombre
    def setName(self, name):
        self.name = name
    #metodo para setear el simbolo
    def setSymbol(self, symbol):
        self.symbol = symbol
    #metodo para setear el turno
    def setTurn(self, turn):
        self.turn = turn
    #metdo para setear el numero de veces que gano el juego
    def setWon(self, won):
        self.won = won
    #metodo para obtener el nombre
    def getName(self):
        return self.name
    #metodo para obtener el symbolo
    def getSymbol(self):
        return self.symbol
    #metodo para obtener el turno
    def getTurn(self):
        return self.turn
    #metodo para obtener las veces qque gano el juego
    def getWon(self):
        return self.won
    #Procedimiento que imprime el nombre anteponiendo Ganador
    def win(self):
        print("Ganador", self.name)

    # Procedimiento que imprime el nombre anteponiendo Perdedro
    def looser(self):
        print("Perdedor", self.name)
    #Procedimiento que imprime la clase
    def getPlayer(self):
        print(self.name)
        print(self.symbol)
        print(self.turn)
        print(self.won)

