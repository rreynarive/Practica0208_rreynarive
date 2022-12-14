def tabla_mul(num):
    if int(num) in range(1, 11):
        file = open("tabla"+str(num)+".txt", "w")
        for i in range(1, 11):
            file.write("{} x {} = {}\n".format(num, i, int(num) * int(i)))
        file.close()
    return


num = input("Escribe un numero entre 1 al 10:\n")
tabla_mul(num)

