import urllib.request
def leer_url(url):
    file = urllib.request.urlopen(url)
    with open(file)
    for linea in file:
        linea_deco = linea.decode("utf-8")
        print(linea_deco)
    return


url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true "