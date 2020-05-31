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
#Mo de juego Humano versus Maquina
def PlayerVsMachine():
    print('\n*--------------------------*')
    print('** MODO PLAYER vs MACHINE **')
    print('*--------------------------*\n')
    print('Antes de empezar a jugar si tiene duda de las instrucciones del juego ingrese el  siguiente comando -i o -I y si necesita ayuda ingrese el siguiente comando -h o -H')
    player1 = input("Ingrese nombre para PLAYER 1: ")
    while True:
        if player1 == '-i' or player1 == '-I':
            Inst()
            player1 = input("Ingrese nombre para PLAYER 1: ")
        elif player1 == '-h' or player1 == '-H':
            Help()
            player1 = input("Ingrese nombre para PLAYER 1: ")
        else:
            break
    player1 = Player(player1)
    print("Ingrese nombre para PLAYER 2: MACHINE")
    player2 = Player("MACHINE", 1, 1)
    sizeT = input('Ingrese el tamaño del tablero: ')
    print()
    while True:
        if sizeT == '-i' or sizeT == '-I':
            Inst()
            sizeT = input('Ingrese el tamaño del tablero: ')
        elif sizeT == '-h' or sizeT == '-H':
            Help()
            sizeT = input('Ingrese el tamaño del tablero: ')
        else:
            break
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
                    move = int(input("Turno de -> " + player.getName()+ " elija una columna: "))
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