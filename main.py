# se importan las funciones de paises.py
from archivos import cargar_paises
from paises import agregar_pais
from paises import modificar_pais
from paises import filtrar_por_continente
paises = cargar_paises("datos/paises.csv")

resultado = filtrar_por_continente (paises, "américa")

for pais in resultado:
    print(pais["nombre"])