def buildBoard(filas: int, columnas: int):
    board = []
    for x in range(0,filas):
        columns = []
        for j in range(0, columnas):
            columns.append(None)
        board.append(columns)
    return board