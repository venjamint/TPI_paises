from archivos import cargar_paises
from paises import buscar_paises

paises = cargar_paises("datos/paises.csv")

resultados = buscar_paises(paises, "arg")

for pais in resultados:
    print(pais["nombre"])