# se importan las funciones  
#de paises.py
from archivos import cargar_paises
from paises import agregar_pais
from paises import modificar_pais
from paises import filtrar_por_continente
#de estadisticas.py
from estadisticas import promediador
from estadisticas import pais_menor_poblacion
from estadisticas import pais_menor_poblacion
from estadisticas import paises_x_continente
paises = cargar_paises("datos/paises.csv")
###################################################
#menu
def mostrar_menu():
    print("\n========== GESTIÓN DE PAÍSES ==========")
    print("1. Agregar país")
    print("2. Modificar país")
    print("3. Buscar país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Estadísticas")
    print("7. Salir")
    print("=======================================")

def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                print("Finalizando programa...")
                break
            case _:
                print("Opción inválida")

main()