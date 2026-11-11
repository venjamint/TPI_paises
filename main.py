# se importan las funciones de paises.py
from archivos import cargar_paises
from paises import agregar_pais
from paises import modificar_pais

paises = cargar_paises("datos/paises.csv")
modificar_pais(paises, "Argentina", 47000000, 2780400)

for pais in paises:
    if pais["nombre"] == "Argentina":
        print(pais)

modificar_pais(paises, "Brasil", -500, 8515767)
modificar_pais(paises, "Brasil", 213993437, "abc")
modificar_pais(paises, "Uruguay", 3500000, 176215)