import csv
def cargar_paises (ruta):
    paises= []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            formato  = ["nombre","poblacion","superficie", "continente" ]
            if lector.fieldnames != formato:
                print("ERROR: El formato del archivo CSV es incorrecto.")
                return None
            for linea in lector:
                try:
                    linea["poblacion"] = int(linea["poblacion"])
                    linea["superficie"] = int(linea["superficie"])

                    if linea["poblacion"] <= 0 or linea["superficie"] <= 0:
                        print("ERROR: Se encontraron valores no válidos.")
                        return None

                    paises.append(linea)
                except (ValueError, TypeError):
                    print("ERROR: Se encontraron datos numéricos inválidos.")
                    return None
        return paises
    except FileNotFoundError:
        print("ERROR: No se encontró el archivo CSV.")
        return None
    except OSError:
        print("ERROR: No se pudo acceder al archivo.")
        return None
    
def guardar_paises (ruta, paises):
    formato  = ["nombre","poblacion","superficie", "continente" ]
 
    with open (ruta, "w", newline= "",encoding ="utf-8") as archivo:
       escritor = csv.DictWriter(archivo, fieldnames= formato)
       escritor.writeheader()      
       escritor.writerows(paises)

 

 