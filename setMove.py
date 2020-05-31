#Realiza el movimiento de el jugador
def setMove(board, column:int, value:int):
    validMove = False
    rows = len(board) -1
    while rows >= 0:
        if board[rows][column] is None:
            board[rows][column] = value
            validMove = True
            break
        rows -= 1
    return validMove