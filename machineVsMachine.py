from searchWinner import searchWinner
from moveMachine import moveMachine
from buildBoard import buildBoard
from drawBoard import drawBoard
from sizeBoard import sizeBoar
from instructions import Inst
from setMove import setMove
from player import Player
from help import Help

import random
def MachineVsMachine():
    print('\n*--------------------------*')
    print('** MODO PLAYER vs MACHINE **')
    print('*--------------------------*\n')
    print('Antes de empezar a jugar si tiene duda de las instrucciones del juego ingrese el  siguiente comando -i o -I y si necesita ayuda ingrese el siguiente comando -h o -H')
    print("Ingrese nombre para PLAYER 1: MACHINE A")
    player1 = Player("MACHINE A")
    print("Ingrese nombre para PLAYER 2: MACHINE B")
    player2 = Player("MACHINE B", 1, 1)
    a = random.randint(5,10)
    b = random.randint(6,10)
    sizeT = str(a) + "X" + str(b)
    print("Ingrese el tamaño del tablero:",sizeT)
    #sizeT = input('Ingrese el tamaño del tablero: ')
    print()
    sizeT = sizeBoar(sizeT)
    player = player1 if (random.randint(0,100) % 2 == 0) else player2
    aux = player.getTurn()
    stop = (sizeT[0] * sizeT[1]) + player.getTurn()
    while True:
        board = buildBoard(sizeT[0],sizeT[1])
        drawBoard(board)
        while True:
            player = player1 if (aux % 2 == 0) else player2
            try:
                if player.getTurn() == 1:
                    move = moveMachine(board, player.getSymbol())
                    if move is None:
                        move = moveMachine(board, player1.getSymbol())
                    print("Turno de -> " + player.getName() + " elija una columna: " + str(move))
                else:
                    #move = int(input("Turno de -> " + player.getName()+ " elija una columna: "))
                    move = moveMachine(board, player2.getSymbol())
                    if move is None:
                        move = moveMachine(board, player.getSymbol())
                    print("Turno de -> " + player.getName() + " elija una columna: " + str(move))
                if 0 < move <= len(board[0]):
                    move -= 1
                    if setMove(board, move, player.getSymbol()):
                        if searchWinner(board, player.getSymbol()):
                            drawBoard(board)
                            print("JUEGO TERMINADO", player.getName(), "GANÓ")
                            if player.getTurn() == 0:
                                player1.setWon(player1.getWon() + 1)
                            else:
                                player2.setWon(player2.getWon() + 1)
                            break
                        drawBoard(board)
                        aux += 1
                    else:
                        print("Columna llena")
                    if aux == stop:
                        print("JUEGO EMPATADO....")
                        break
                else:
                    print("Columna fuera de rango")
            except ValueError:
                print("Columna no válida")
        playAgain = input("¿Otra partida (s)? ").lower()
        if playAgain == 's':
            aux = player.getTurn()
            stop = (sizeT[0] * sizeT[1]) + player.getTurn()
        else:
            print(player1.getName(), player1.getWon(), player2.getName(), player2.getWon())
            print()
            break