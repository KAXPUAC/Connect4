#Procedimiento que imprime las instrucciones de el juego
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