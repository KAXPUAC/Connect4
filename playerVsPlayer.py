from searchWinner import searchWinner
from buildBoard import buildBoard
from drawBoard import drawBoard
from sizeBoard import sizeBoar
from instructions import Inst
from setMove import setMove
from player import Player
from help import Help
import random
#Modo de Juego Humano versus Humano
def PlayerVsPlayer():
    print('\n*-------------------------*')
    print('** MODO PLAYER vs PLAYER **')
    print('*-------------------------*\n')
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
    player2 = input("Ingrese nombre para PLAYER 2: ")
    while True:
        if player2 == '-i' or player2 == '-I':
            Inst()
            player2 = input("Ingrese nombre para PLAYER 2: ")
        elif player2 == '-h' or player2 == '-H':
            Help()
            player2 = input("Ingrese nombre para PLAYER 2: ")
        else:
            break
    player2 = Player(player2, 1, 1)
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
                move = input("Turno de -> " + player.getName() + " elija una columna: ")
                if move == '-i' or move == '-I':
                    Inst()
                    continue
                elif move == '-h' or move == '-H':
                    Help()
                    continue
                move = int(move)
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
                            #player.setWon(player.getWon() + 1)
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