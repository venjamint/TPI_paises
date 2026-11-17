import csv
def cargar_paises (ruta):
    paises= []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            formato: list[str]  = ["nombre","poblacion","superficie", "continente" ]
        for linea in lector:
            linea["poblacion"] = int(linea["poblacion"])
            linea["superficie"] = int(linea["superficie"])
            paises.append(linea)
        return paises
def guardar_paises (ruta, paises):
    formato  = ["nombre","poblacion","superficie", "continente" ]
 
    with open (ruta, "w", newline= "",encoding ="utf-8") as archivo:
       escritor = csv.DictWriter(archivo, fieldnames= formato)
       escritor.writeheader()      
       escritor.writerows(paises)

 

 