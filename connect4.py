def main():
    from drawBoard import drawBoard
    import random
    import re
    tamanoTablero = ""
    while True:
        tamanoTablero = input("Ingrese el tamaño de tablero: ").strip()
        uno = re.compile("[5-9]{1}\*[6-9]{1}")
        unno = re.compile("[5-9]{1}[x|X][6-9]{1}")
        dos = re.compile("10\*10")
        doss = re.compile("10{1}[x|X]10{1}")
        if uno.fullmatch(tamanoTablero):
            tamanoTablero = tamanoTablero.split("*")
            break
        elif unno.fullmatch(tamanoTablero):
            tamanoTablero = tamanoTablero.split("x")
            if len(tamanoTablero) != 2:
                tamanoTablero = tamanoTablero[0].split("X")
            break
        elif dos.fullmatch(tamanoTablero):
            tamanoTablero = tamanoTablero.split("*")
            break
        elif doss.fullmatch(tamanoTablero):
            tamanoTablero = tamanoTablero.split("x")
            if len(tamanoTablero) != 2:
                tamanoTablero = tamanoTablero[0].split("X")
            break
        else:
            print("Error")
    global columnas, filas
    columnas = int(tamanoTablero[0])
    filas = int(tamanoTablero[1])
    tablero = []
    for x in range(0,filas):
        body = []
        for j in range(0, columnas):
            body.append(None)
        tablero.append(body)
    nombreJugador1 = input("Ingrese nombre para Jugador 1: ")
    nombreJugador2 = input("Ingrese nombre para Jugador 2: ")
    print(nombreJugador1)
    print(nombreJugador2)
    drawBoard(columnas, filas, tablero)
    j = 100
    #while True:
    while j > 0:
        colocar = (random.randint(1,columnas) - 1)
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
main()
def construye_tabla_formatos():
    for estilo in range(8):
        for colortexto in range(30,38):
            cad_cod = ''
            for colorfondo in range(40,48):
                fmto = ';'.join([str(estilo),
                                 str(colortexto),
                                 str(colorfondo)])
                cad_cod+="\033["+fmto+"m "+fmto+" \033[0m"
            print(cad_cod)
        print('\n')
#construye_tabla_formatos()