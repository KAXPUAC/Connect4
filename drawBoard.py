def drawBoard(col: int, fil: int, tabla):
    from colorama import init, Fore, Back, Style
    head = ''
    final = ''
    for x in range(col):
        head = head + " " + str(x + 1)
    for i in range(fil):
        tablero = ''
        for j in range(col):
            tablero = tablero[0:len(tablero) - 1] + "|"
            if tabla[i][j] == 0:
                tablero += Fore.RED + "O"
            elif tabla[i][j] == 1:
                tablero += Fore.GREEN + "O"
            else:
                tablero += " "
            tablero += Fore.WHITE + "|"
        if i == 0:
            print(head)
        print(tablero)
    for x in range(0, col):
        final = final + "+-"
    final = final + "+"
    print(final)