def drawBoard(col: int, fil: int, tabla):
    head = ''
    final = ''
    for x in range(col):
        head = head + " " + str(x + 1)
    for i in range(fil):
        tablero = ''
        for j in range(col):
            tablero = tablero[0:len(tablero) - 1] + "|" + ("o" if (tabla[i][j]) == "o" else " ") + "|"
        if i == 0:
            print(head)
        print(tablero)
    for x in range(0, col):
        final = final + "+-"
    final = final + "+"
    print(final)
def main():
    import re
    tamanoTablero = ""
    while True:
        tamanoTablero = input("Ingrese el tamaño de tablero: ").strip()
        uno = re.compile("[5-9]{1}\*[5-9]{1}")
        unno = re.compile("[5-9]{1}[x|X][5-9]{1}")
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
    columnas = int(tamanoTablero[0])
    filas = int(tamanoTablero[1])
    tablero = [[None] * columnas] * filas
    drawBoard(columnas, filas, tablero)
    while True:
        drawBoard(columnas, filas,tablero)
        break
main()
