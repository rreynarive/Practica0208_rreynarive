import os

def tabla_mul(num):
    if os.path.isfile("tabla" + str(num) + ".txt"):
        with open("tabla" + str(num) + ".txt", "r") as file:
            print(file.read())
    else:
        print("El fichero {} no existe".format("tabla" + str(num) + ".txt"))
    return


num = input("Escribe un numero entre 1 al 10:\n")
tabla_mul(num)
