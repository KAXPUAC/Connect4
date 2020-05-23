def drawBoard(col: int, fil: int, tabla):
    #from colorama import init, Fore, Back, Style
    head = ''
    final = ''
    for x in range(col):
        head = head + " " + str(x + 1)
    for i in range(fil):
        tablero = ''
        for j in range(col):
            tablero = tablero[0:len(tablero) - 1] + "|"
            if tabla[i][j] == 0:
                tablero += "X"
            elif tabla[i][j] == 1:
                tablero += "O"
            else:
                tablero += " "
            tablero += "|"
        if i == 0:
            print(head)
        print(tablero)
    for x in range(0, col):
        final = final + "+-"
    final = final + "+"
    print(final)

def sizeTable(sizeT):
    import re
    while True:
        sizeT.strip()
        uno = re.compile("[5-9]{1}\*[6-9]{1}")
        unno = re.compile("[5-9]{1}[x|X][6-9]{1}")
        dos = re.compile("10\*10")
        doss = re.compile("10{1}[x|X]10{1}")
        if uno.fullmatch(sizeT):
            sizeT = sizeT.split("*")
            return sizeT
        elif unno.fullmatch(sizeT):
            sizeT = sizeT.split("x")
            if len(sizeT) != 2:
                sizeT = sizeT[0].split("X")
            return sizeT
        elif dos.fullmatch(sizeT):
            sizeT = sizeT.split("*")
            return sizeT
        elif doss.fullmatch(sizeT):
            sizeT = sizeT.split("x")
            if len(sizeT) != 2:
                sizeT = sizeT[0].split("X")
            return sizeT
        else:
            return sizeT

def PlayerVsPlayer():
    print('\n---------------------------')
    print('** MODO PLAYER vs PLAYER **\n')
    player1 = input("Ingrese nombre para PLAYER 1: ")
    player2 = input("Ingrese nombre para PLAYER 2: ")
    print(player1)
    print(player2)

def PlayerVsMachine():
    print('\n-------------------------------')
    print('**MODO MACHINE vs MACHINE**\n')
    player = input('Ingrese nombre para PLAYER')
    print(player)
    machine = input('Ingrese nombre para MACHINE')
    print(machine)

def MachineVsMachine():
    print('\n-------------------------------')
    print('**MODO MACHINE vs MACHINE**\n')
    print('MACHINE_1')
    print('MACHINE_2')
    #from drawBoard import drawBoard
    import random
    sizeT = input("Ingrese el tamaño de tablero: ")
    if len(sizeT) > 0:
        sizeT = sizeTable(sizeT)
        global columnas, filas
        columnas = int(sizeT[0])
        filas = int(sizeT[1])
        tablero = []
        for x in range(0,filas):
            body = []
            for j in range(0, columnas):
                body.append(None)
            tablero.append(body)

        print(tablero)
        drawBoard(columnas, filas, tablero)
        j = 5
    #while True:
        while j > 0:
            colocar = (random.randint(1,columnas) - 1)
            colocar = 3
        #print("Columna", colocar + 1)
        #jugador = random.randint(0,1)
            jugador = j % 2
        #print("Valor", jugador)
            i = len(tablero[colocar]) - 1
            while i > 0:
                if tablero[i][colocar] is None:
                    tablero[i][colocar] = jugador
                    break
                i -= 1
            drawBoard(columnas, filas,tablero)
            j -= 1
    else:
        print("ERROR: Ingrese numeros y el tablero puede tener medidas de 5X6 hasta 10X10")

def player():
    aux = 0
    while True:
        colocar = int(input("Ingrese columa: ")) - 1
        jugador = aux % 2
        i = len(tablero[colocar]) - 1
        while i > 0:
            if tablero[i][colocar] is None:
                tablero[i][colocar] = jugador
                break
            i -= 1
        drawBoard(columnas, filas, tablero)

        aux += 1



def main():
   # from drawBoard import drawBoard
    exit = True
    while exit:
        print('\n*** Bienvenido al juego CONNECT4 ***')
        print('====================================')
        opcion = 0
        while(opcion != 5) :
                print('\nModos de juego:')
                print('(1) PLAYER vs PLAYER\n(2) PLAYER vs MACHINE\n(3) MACHINE vs MACHINE\n(4) HELP\n(5) EXIT')
                try:
                    opcion = int(input("Ingrese una opcion: "))
                    if opcion == 1:
                        print("opcion 1")
                        PlayerVsPlayer()
                    elif opcion == 2:
                        print("opcion 2")
                        PlayerVsMachine()
                    elif opcion == 3:
                        print("opcion 3")
                        MachineVsMachine()
                    elif opcion == 4:
                        print("HELP")    
                    elif opcion == 5:   
                        print("\nSaliendo del juego ...")
                        exit = False
                    else:
                        print("\nERROR: Opcion invalida! Solo hay opciones 1, 2, 3, 4, y 5\n")
                except ValueError:
                    print("\nERROR: Opcion invalida! No ingreso un numero entero\n")
                    opcion = 0
main()