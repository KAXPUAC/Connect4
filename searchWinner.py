def searchWinner(board, symbol: int):
    winner = False
    columns = len(board[0])
    #Verificar Filas
    for c in range(columns-3):
        for j in range(len(board)):
            if board[j][c] == symbol and board[j][c + 1] == symbol and board[j][c + 2] == symbol and board[j][c + 3] == symbol:
                return True
    #verificar Columnas
    for c in range(columns):
        for j in range(len(board)-3):
            if board[j][c] == symbol and board[j + 1][c] == symbol and board[j + 2][c] == symbol and board[j + 3][c] == symbol:
                return True
    #Verifica Digonales invertida \
    for c in range(columns - 3):
        for j in range(len(board)-3):
            if board[j][c] == symbol and board[j + 1][c + 1] == symbol and board[j + 2][c + 2] == symbol and board[j + 3][c + 3] == symbol:
                return True
    #Verifica Digonales normales /
    for c in range(columns - 3):
        for j in range(3,len(board)):
            if board[j][c] == symbol and board[j - 1][c + 1] == symbol and board[j - 2][c + 2] == symbol and board[j - 3][c + 3] == symbol:
                return True

    return winner