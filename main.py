from archivos import cargar_paises
from paises import agregar_pais
 
paises = cargar_paises("datos/paises.csv")

# Prueba 1: agregar un país válido
agregar_pais(paises, "Chile", 19600000, 756102, "América")

# Mostrar resultado
for pais in paises:
    print (pais["nombre"])