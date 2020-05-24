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
            if tabla[i][j] != 0 and tabla[i][j]!=1:
                tablero += " "
            elif tabla[i][j] == 0:
                tablero += "X"
            elif tabla[i][j] == 1:
                tablero += "O"
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

def Inst():
    print('\n*------------------------------------*')
    print('** INSTRUCCIONES DEL JUEGO CONNECT4 **')
    print('*------------------------------------*\n')
    print('El juego está formado por un tablero, y fichas de forma "O" y "X" .Es un juego para dos jugadores y cada jugador tiene asignado una ficha. El objetivo de ​Connect4​, como su nombre lo dice,consiste en conectar 4 fichas del mismo unir una línea, en cualquier dirección, horizontal, vertical, y diagonalmente (hacia ambos lados). El jugador que forme la fila de cuatro fichas primero ganará. Las reglas del juego no son muy complicadas:\n')
    print('* El jugador que juega primero se escoge al azar siendo utilizando la ficha "O".')
    print('* Cada jugador tira una sola ficha por turno.')
    print('* El tablero se compone de columnas,no de filas. Eso quiere decir que las fichas solo pueden introducirse en la parte de arriba de una columna,y caer hasta llegar a la parte más baja o encima de otra ficha.')
    print('* El juego se gana solo si uno de los jugadores logra forman una linea de cuatro fichas del mismo.')
    print('* Si el tablero se llena de fichas y no hay ganador, el juego quedó empatado.\n')
    print('--> SI NECESITA AYUDA COMO JUGAR INGRESE LA OPCION (5) HELP')
    print('*------------------------------------*\n')

def PlayerVsPlayer():
    import random 
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
    sizeT = sizeTable(sizeT)
    global columnas, filas, cont
    columnas = int(sizeT[0])
    filas = int(sizeT[1])
    cont = 0
    tablero = []
    for x in range(0,filas):
        body = []
        for j in range(0, columnas):
            body.append(None)
            cont +=1
        tablero.append(body)
    drawBoard(columnas, filas, tablero)
    ss=random.randint(0,1)
    selec = ['O','X']
    p1 = selec[ss]
    if ss == 0:
        p2 = selec[1]
        inicia = player1
        sigue = player2
    else:
        p2 = selec[0]
        inicia = player2
        sigue = player1 
    print('Tiros faltantes:',cont)
    print('PLAYER 1:',player1,'->',p1)
    print('PLAYER 2:',player2,'->', p2) 
    while cont !=0:
        cont -= 1
        jugador = cont % 2
        if jugador == 0:
            Str = input('Toca tirar a '+ sigue + ' escoger una columna: ')
            while True:
                if Str == '-i' or Str == '-I':
                    Inst()
                    Str = input('Toca tirar a '+ sigue + ' escoger una columna: ')
                elif Str == '-h' or Str == '-H':
                    Help()
                    Str = input('Toca tirar a '+ sigue + ' escoger una columna: ')
                else:    
                    colocar = int(Str) - 1
                    print()
                    break
        else:
            Str = input('Toca tirar a '+ inicia + ' escoger una columna: ')
            while True:
                if Str == '-i' or Str == '-I':
                    Inst()
                    Str = input('Toca tirar a '+ inicia + ' escoger una columna: ')
                elif Str == '-h' or Str == '-H':
                    Help()
                    Str = input('Toca tirar a '+ inicia + ' escoger una columna: ')
                else:
                    colocar = int(Str) - 1
                    print()
                    break

        if colocar >= 0 and colocar < columnas :
            i = filas - 1 
            while i >= 0:
                if tablero[i][colocar] is None:
                    tablero[i][colocar] = jugador
                    break
                i -= 1
            if i != -1 :
                drawBoard(columnas, filas, tablero)
                print('Tiros faltantes:',cont)
            else:
                print('ERROR: Columna llena escoger otra...\n')
                cont +=1
        else:
            print('ERROR: Verificar que el rango de columnas es de 1 a',columnas,'...\n')
            cont +=1

def PlayerVsMachine():
    import random 
    print('\n*--------------------------*')
    print('** MODO PLAYER vs MACHINE **')
    print('*--------------------------*\n')
    print('Antes de empezar a jugar si tiene duda de las instrucciones del juego ingrese el  siguiente comando -i o -I y si necesita ayuda ingrese el siguiente comando -h o -H')
    player1 = input("Ingrese nombre para PLAYER: ")
    while True:
        if player1 == '-i' or player1 == '-I':  
            Inst()
            player1 = input("Ingrese nombre para PLAYER: ")
        elif player1 == '-h' or player1 == '-H':
            Help()
            player1 = input("Ingrese nombre para PLAYER: ")
        else:
            break
    player2 = 'MACHINE'
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
    sizeT = sizeTable(sizeT)
    global columnas, filas, cont
    columnas = int(sizeT[0])
    filas = int(sizeT[1])
    cont = 0
    tablero = []
    for x in range(0,filas):
        body = []
        for j in range(0, columnas):
            body.append(None)
            cont +=1
        tablero.append(body)
    drawBoard(columnas, filas, tablero)
    ss=random.randint(0,1)
    selec = ['O','X']
    p1 = selec[ss]
    if ss == 0:
        p2 = selec[1]
        inicia = player1
        sigue = player2
    else:
        p2 = selec[0]
        inicia = player2
        sigue = player1 
    print('Tiros faltantes:',cont)
    print('PLAYER:',player1,'->',p1)
    print(player2,'->', p2) 
    while cont !=0:
        cont -= 1
        jugador = cont % 2
        if jugador == 0:
            if sigue == 'MACHINE':
                print('Toca tirar a MACHINE')
                colocar = (random.randint(1,columnas) - 1)
                print()
            else:
                Str = input('Toca tirar a '+ sigue + ' escoger una columna: ')
                while True:
                    if Str == '-i' or Str == '-I':
                        Inst()
                        Str = input('Toca tirar a '+ sigue + ' escoger una columna: ')
                    elif Str == '-h' or Str == '-H':
                        Help()
                        Str = input('Toca tirar a '+ sigue + ' escoger una columna: ')
                    else:
                        break
                colocar = int(Str) - 1
                print()
        else:
            if inicia == 'MACHINE':
                print('Toca tirar a MACHINE')
                colocar = (random.randint(1,columnas) - 1)
                print()
            else:
                Str = input('Toca tirar a '+ inicia + ' escoger una columna: ')
                while True:
                    if Str == '-i' or Str == '-I':
                        Inst()
                        Str = input('Toca tirar a '+ inicia + ' escoger una columna: ')
                    elif Str == '-h' or Str == '-H':
                        Help()
                        Str = input('Toca tirar a '+ inicia + ' escoger una columna: ')
                    else:
                        break
                colocar = int(Str) - 1
                print()
        if colocar >= 0 and colocar < columnas :
            i = filas - 1 
            while i >= 0:
                if tablero[i][colocar] is None:
                    tablero[i][colocar] = jugador
                    break
                i -= 1
            if i != -1 :
                drawBoard(columnas, filas, tablero)
                print('Tiros faltantes:',cont)
            else:
                print('ERROR: Columna llena escoger otra...\n')
                cont +=1
        else:
            print('ERROR: Verificar que el rango de columnas es de 1 a',columnas,'...\n')
            cont +=1

def MachineVsMachine():
    import random 
    print('\n*---------------------------*')
    print('** MODO MACHINE vs MACHINE **')
    print('*---------------------------*\n')
    player1 = 'MACHINE 1'
    player2 = 'MACHINE 2'
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
    sizeT = sizeTable(sizeT)
    global columnas, filas, cont
    columnas = int(sizeT[0])
    filas = int(sizeT[1])
    cont = 0
    tablero = []
    for x in range(0,filas):
        body = []
        for j in range(0, columnas):
            body.append(None)
            cont +=1
        tablero.append(body)
    drawBoard(columnas, filas, tablero)
    ss=random.randint(0,1)
    selec = ['O','X']
    p1 = selec[ss]
    if ss == 0:
        p2 = selec[1]
        inicia = player1
        sigue = player2
    else:
        p2 = selec[0]
        inicia = player2
        sigue = player1 
    print('Tiros faltantes:',cont)
    print(player1,'->',p1)
    print(player2,'->', p2) 
    while cont != 0:
        cont -= 1
        jugador = cont % 2
        if jugador == 0:
            colocar = (random.randint(1,columnas) - 1)
            print('Toca tirar a ' + sigue + ' escoger una columna: ', (colocar + 1))
            print()
        else:
            colocar = (random.randint(1,columnas) - 1)
            print('Toca tirar a ' + inicia + ' escoger una columna: ', (colocar + 1))
            print()
        if colocar >= 0 and colocar < columnas :
            i = filas - 1 
            while i >= 0:
                if tablero[i][colocar] is None:
                    tablero[i][colocar] = jugador
                    break
                i -= 1
            if i != -1 :
                drawBoard(columnas, filas, tablero)
                print('Tiros faltantes:',cont)
            else:
                print('ERROR: Columna llena escoger otra...\n')
                cont += 1
        else:
            print('ERROR: Verificar que el rango de columnas es de 1 a',columnas,'...\n')
            cont += 1

def Help():
    print('\n*---------------------------*')
    print('** HELP DEL JUEGO CONNECT4 **')
    print('*---------------------------*\n')
    print('> Si su opcion es el MODO PLAYER vs PLAYER lo que tiene que hacer es ingresar los nombres de ambos jugadores (el juego se los va pedir uno por uno) luego tiene que ingresar el tamaño del tablero.')
    print('> Si su opcion es el MODO PLAYER vs MACHINE lo que tiene que hacer es ingresar su nombre (cuando el juego se lo pida) luego tiene que ingresar el tamaño del tablero.')
    print('> Si su opcion es el MODO MACHINE vs MACHINE lo unico que tiene que hacer es ingresar el tamaño del tablero.')
    print('\nATENCION!!!')
    print('-> El jugador que le toca la ficha "O" es el que inicia.')
    print('-> El tamaño del tablero tiene una medida minima de 5X6 y maxima de 10X10 de lo contrario el juego le va dar ERROR.')
    print('-> El juego le va indicar por su nombre a quien le toca ingresar una ficha.')
    print('-> Procure que el numero de columna que ingrese, en su turno, este en el rango de columnas del tablero de lo contrario le va dar ERROR.')
    print('-> Si una de las columnas esta llena, ingrese la ficha en otra columna de lo contrario le va dar ERROR.')
    print('-> Si aun tiene dudas de como son las instrucciones del juego ingrese la opcion (1) INSTRUCCIONES .')
    print('*---------------------------*\n')

def main():
   # from drawBoard import drawBoard
    exit = True
    while exit:
        print('\n====================================')
        print('*** Bienvenido al juego CONNECT4 ***')
        print('====================================')
        opcion = 0
        while(opcion != 6) :
                print('(1) INSTRUCCIONES\n(2) PLAYER vs PLAYER\n(3) PLAYER vs MACHINE\n(4) MACHINE vs MACHINE\n(5) HELP\n(6) EXIT')
                try:
                    opcion = int(input("Ingrese una opcion: "))
                    if opcion == 1:
                        Inst()
                    elif opcion == 2:
                        PlayerVsPlayer()
                    elif opcion == 3:
                        PlayerVsMachine()
                    elif opcion == 4:
                        MachineVsMachine()
                    elif opcion == 5:
                        Help()    
                    elif opcion == 6:   
                        print('\nGracias por visitar Connect4 !!! ')
                        print('Saliendo del juego ...')
                        exit = False
                    else:
                        print('\nERROR: Opcion invalida! Solo hay opciones 1, 2, 3, 4, 5 y 6\n')
                except ValueError:
                    print('\nERROR: Opcion invalida! No ingreso un numero entero\n')
                    opcion = 0
main()