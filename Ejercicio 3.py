import os

def tabla_multiplicar(num, linea):
    if os.path.isfile("tabla" + str(num) + ".txt"):
        with open("tabla" + str(num) + ".txt", "r") as file:
            lista = file.readlines()
            print(lista[int(linea) - 1])
    else:
        print("El fichero {} no existe".format("tabla" + str(num) + ".txt"))
    return


num = input("Escribe un numero entre 1 al 10:\n")
linea = input("Introduzca la linea que quiera consultar:\n")

tabla_multiplicar(num, linea)