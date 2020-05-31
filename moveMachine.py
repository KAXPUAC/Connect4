import random
def moveMachine(board, symbol: int):
    columns = len(board[0])
    # Verificar Filas
    for c in range(columns - 3):
        for j in range(len(board)):
            if board[j][c] == symbol and board[j][c + 1] == symbol and board[j][c + 2] == symbol and board[j][c + 3] is None:
                return c + 3 + 1
            if board[j][c] is None and board[j][c + 1] == symbol and board[j][c + 2] == symbol and board[j][c + 3] == symbol:
                return c + 1
            if board[j][c] == symbol and board[j][c + 1] is None and board[j][c + 2] == symbol and board[j][c + 3] == symbol:
                return c + 1 + 1
            if board[j][c] == symbol and board[j][c + 1] == symbol and board[j][c + 2] is None and board[j][c + 3] == symbol:
                return c + 2 + 1
    # verificar Columnas
    for c in range(columns):
        for j in range(len(board) - 3):
            if board[j][c] == symbol and board[j + 1][c] == symbol and board[j + 2][c] == symbol and board[j + 3][c] is None:
                return c + 1
            if board[j][c] is None and board[j + 1][c] == symbol and board[j + 2][c] == symbol and board[j + 3][c] == symbol:
                return c + 1
            if board[j][c] == symbol and board[j + 1][c] is None and board[j + 2][c] == symbol and board[j + 3][c] == symbol:
                return c + 1
            if board[j][c] == symbol and board[j + 1][c] == symbol and board[j + 2][c] is None and board[j + 3][c] == symbol:
                return c + 1
    # Verifica Digonales invertida \
    for c in range(columns - 3):
        for j in range(len(board) - 3):
            if board[j][c] == symbol and board[j + 1][c + 1] == symbol and board[j + 2][c + 2] == symbol and board[j + 3][c + 3] is None:
                return c + 3 + 1
            if board[j][c] is None and board[j + 1][c + 1] == symbol and board[j + 2][c + 2] == symbol and board[j + 3][c + 3] == symbol:
                return c + 1
            if board[j][c] == symbol and board[j + 1][c + 1] is None and board[j + 2][c + 2] == symbol and board[j + 3][c + 3] == symbol:
                return c + 1 + 1
            if board[j][c] == symbol and board[j + 1][c + 1] == symbol and board[j + 2][c + 2] is None and board[j + 3][c + 3] == symbol:
                return c + 2 + 1
    # Verifica Digonales normales /
    for c in range(columns - 3):
        for j in range(3, len(board)):
            if board[j][c] == symbol and board[j - 1][c + 1] == symbol and board[j - 2][c + 2] == symbol and board[j - 3][c + 3] is None:
                return c + 3 + 1
            if board[j][c] is None and board[j - 1][c + 1] == symbol and board[j - 2][c + 2] == symbol and board[j - 3][c + 3] == symbol:
                return c + 1
            if board[j][c] == symbol and board[j - 1][c + 1] is None and board[j - 2][c + 2] == symbol and board[j - 3][c + 3] == symbol:
                return c + 1 + 1
            if board[j][c] == symbol and board[j - 1][c + 1] == symbol and board[j - 2][c + 2] is None and board[j - 3][c + 3] == symbol:
                return c + 2 + 1

    return None if symbol == 1 else random.randint(1,columns)