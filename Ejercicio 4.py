import urllib.request
letra = 0
def leer_url(url):
    file = urllib.request.urlopen(url)
    for linea in file:
        linea_deco = linea.decode("utf-8")
        for letra in linea:
            letra += 1
            print(letra)
        print(linea_deco)
    return


url = "http://textfiles.com/adventure/aencounter.txt"
leer_url(url)