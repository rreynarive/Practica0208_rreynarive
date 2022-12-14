import urllib.request

def leer_url(url):
    file = urllib.request.urlopen(url)
    for linea in file:
        linea_deco = linea.decode("uft-8")
        print(linea_deco)
    return


url = "https://drive.google.com/drive/my-drive"
leer_url(url)