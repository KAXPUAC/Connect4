#Archivo Principal
from help import Help
from instructions import Inst
from playerVsPlayer import PlayerVsPlayer
from playerVsMachine import PlayerVsMachine
from machineVsMachine import MachineVsMachine
#menu de el juego
def menu():
    while True:
        print('\n====================================')
        print('*** Bienvenido al juego CONNECT4 ***')
        print('====================================')
        while True:
            print('(1) INSTRUCCIONES')
            print('(2) PLAYER vs PLAYER')
            print('(3) PLAYER vs MACHINE')
            print('(4) MACHINE vs MACHINE')
            print('(5) HELP')
            print('(6) EXIT')
            try:
                option = int(input("Ingrese una opcion: "))
                if option == 1:
                    Inst()
                elif option == 2:
                    PlayerVsPlayer()
                elif option == 3:
                    PlayerVsMachine()
                elif option == 4:
                    MachineVsMachine()
                elif option == 5:
                    Help()
                elif option == 6:
                    print('\nGracias por visitar Connect4 !!! ')
                    print('Saliendo del juego ...')
                    break
                else:
                    print('\nERROR: Opcion invalida! Solo hay opciones 1, 2, 3, 4, 5 y 6\n')
            except ValueError:
                print('\nERROR: Opcion invalida! No ingreso un numero entero\n')
        break
menu()