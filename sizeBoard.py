#Veifica y devuelve el tamaño de el tablero
import re
def sizeBoar(sizeT):
    size = [5,6]
    while True:
        sizeT.strip()
        uno = re.compile("[5-9]{1}\*[6-9]{1}")
        unno = re.compile("[5-9]{1}[x|X][6-9]{1}")
        diez = re.compile("[5-9]{1}[x|X]10{1}")
        dieez = re.compile("[5-9]{1}\*10{1}")
        diezreverse = re.compile("10{1}[x|X][6-9]{1}")
        dieezreverse = re.compile("10{1}\*[6-9]{1}")
        dos = re.compile("10\*10")
        doss = re.compile("10{1}[x|X]10{1}")
        if uno.fullmatch(sizeT):
            sizeT = sizeT.split("*")
            size[0] = int(sizeT[0])
            size[1] = int(sizeT[1])
            return size
        elif unno.fullmatch(sizeT):
            sizeT = sizeT.split("x")
            if len(sizeT) != 2:
                sizeT = sizeT[0].split("X")
            size[0] = int(sizeT[0])
            size[1] = int(sizeT[1])
            return size
        elif dos.fullmatch(sizeT):
            sizeT = sizeT.split("*")
            size[0] = int(sizeT[0])
            size[1] = int(sizeT[1])
            return size
        elif doss.fullmatch(sizeT):
            sizeT = sizeT.split("x")
            if len(sizeT) != 2:
                sizeT = sizeT[0].split("X")
            size[0] = int(sizeT[0])
            size[1] = int(sizeT[1])
            return size
        elif diez.fullmatch(sizeT):
            sizeT = sizeT.split("x")
            if len(sizeT) != 2:
                sizeT = sizeT[0].split("X")
            size[0] = int(sizeT[0])
            size[1] = int(sizeT[1])
            return size
        elif dieez.fullmatch(sizeT):
            sizeT = sizeT.split("*")
            size[0] = int(sizeT[0])
            size[1] = int(sizeT[1])
            return size
        elif diezreverse.fullmatch(sizeT):
            sizeT = sizeT.split("x")
            if len(sizeT) != 2:
                sizeT = sizeT[0].split("X")
            size[0] = int(sizeT[0])
            size[1] = int(sizeT[1])
            return size
        elif dieezreverse.fullmatch(sizeT):
            sizeT = sizeT.split("*")
            size[0] = int(sizeT[0])
            size[1] = int(sizeT[1])
            return size
        else:
            print("Tamaño de tablero no válido")
            sizeT = input('Ingrese el tamaño del tablero: ')
