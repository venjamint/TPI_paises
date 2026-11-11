import csv
def cargar_paises (ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        paises = []
        for linea in lector:
            linea["poblacion"] = int(linea["poblacion"])
            linea["superficie"] = int(linea["superficie"])
            paises.append(linea)
        return paises


 
 
 