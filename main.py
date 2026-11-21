import os
# se importan las funciones  
 #de archivos.py
from archivos import cargar_paises, guardar_paises
#de paises.py
from paises import (agregar_pais, 
mostrar_paises,
modificar_pais,
buscar_paises,
filtrar_por_continente, 
filtrar_por_poblacion, 
filtrar_por_superficie,
normalizar_texto,
ordenar,
eliminar_pais )
#de estadisticas.py
from estadisticas import (promediador,
pais_menor_poblacion,
 pais_mayor_poblacion,
paises_x_continente)

####################################################################
#menu
def mostrar_menu():
    print("\n========== GESTIÓN DE PAÍSES ==========")
    print("1. Agregar país")
    print ("2. Eliminar país")
    print("3. Modificar país")
    print("4. Buscar país")
    print("5. Filtrar países")
    print("6. Ordenar países")
    print("7. Estadísticas")
    print("8. Salir")
    print("=======================================")
####################################################################   
#funcion de sub menu para case 4
def menu_filtros(paises):

    while True:
        print("\n========== FILTRAR PAÍSES ==========")
        print("1. Filtrar por continente")
        print("2. Filtrar por población")
        print("3. Filtrar por superficie")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        match opcion:

            case "1":
                continente = pedir_texto("Ingrese el continente: ")
                resultado = filtrar_por_continente(
                    paises, continente
                )
                mostrar_paises(resultado)

            case "2":
                minimo = pedir_entero_positivo("Ingrese la población mínima: ")
                maximo = pedir_entero_positivo("Ingrese la población máxima: ")

                resultado = filtrar_por_poblacion(
                    paises, minimo, maximo
                )
                mostrar_paises(resultado)

            case "3":
                minimo = pedir_entero_positivo("Ingrese la superficie mínima: ")
                maximo = pedir_entero_positivo("Ingrese la superficie máxima: ")

                resultado = filtrar_por_superficie(
                    paises, minimo, maximo
                )
                mostrar_paises(resultado)

            case "4":
                print("volviendo al menu...")
                return

            case _:
                print("ERROR: Opción inválida")
####################################################################
#funcion sub menu case 5
def menu_ordenamientos(paises):

    while True:
        print("\n========== ORDENAR PAÍSES ==========")
        print("1. Ordenar por nombre")
        print("2. Ordenar por población")
        print("3. Ordenar por superficie")
        print("4. Volver al menú principal")

        criterio = input("Seleccione un criterio: ")

        if criterio == "4":
            break
        #Comprobamos que el usuario haya seleccionado una opción válida.
        if criterio not in ("1", "2", "3"):
            print("ERROR: Criterio inválido")
            continue
        #pedimos el orden
        print("\n1. Ascendente")
        print("2. Descendente")
        orden = input("Seleccione el orden: ")
        
        #comprobamos
        if orden not in ("1", "2"):
            print("ERROR: Orden inválido")
            continue

        resultado = ordenar(
            paises,
            int(criterio),
            int(orden)
        )

        mostrar_paises(resultado)
####################################################################
#funcion de sub menu case 6
def menu_estadisticas(paises):

    while True:
        print("\n========== ESTADÍSTICAS ==========")
        print("1. País con mayor población")
        print("2. País con menor población")
        print("3. Promedio de población")
        print("4. Promedio de superficie")
        print("5. Cantidad de países por continente")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        match opcion:

            case "1":
                resultado = pais_mayor_poblacion(paises)

                if resultado is None:
                    print("No hay países registrados.")
                else:
                    print(f"País: {resultado['nombre']}")
                    print(f"Población: {resultado['poblacion']}")

            case "2":
                resultado = pais_menor_poblacion(paises)

                if resultado is None:
                    print("No hay países registrados.")
                else:
                    print(f"País: {resultado['nombre']}")
                    print(f"Población: {resultado['poblacion']}")

            case "3":
                resultado =promediador(paises, "poblacion")

                if resultado is None:
                    print("No se puede calcular el promedio.")
                else:
                    print(f"Promedio de población: {resultado:,.2f}")

            case "4":
                resultado = promediador (paises, "superficie")

                if resultado is None:
                    print("No se puede calcular el promedio.")
                else:
                    print(f"Promedio de superficie: {resultado:,.2f} km²")

            case "5":
                resultado = paises_x_continente(paises)

                if not resultado:
                    print("No hay países registrados.")
                else:
                    print("\nCantidad de países por continente:")

                    for continente, cantidad in resultado.items():
                        print(f"{continente}: {cantidad}")

            case "6":
                break

            case _:
                print("ERROR: Opción inválida")
####################################################################
def main():
    paises = cargar_datos_iniciales()
    if paises is None:
        return
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                nombre = pedir_texto("Ingrese el nombre del país: ")
                poblacion = pedir_entero_positivo("Ingrese la población: ")
                superficie = pedir_entero_positivo("Ingrese la superficie: ")
                continente = pedir_texto("Ingrese el continente: ") 
                
                while continente.lower() not in ("america", "américa", "asia", "europa","africa", "áfrica", "oceania", "oceanía"):
                    print("ERROR: Ingrese un continente válido.")
                    continente = pedir_texto("Ingrese el continente: ")
            # Estandarizar el nombre del continente
                if continente.lower() in ("america", "américa"):
                    continente = "América"
                elif continente.lower() in ("africa", "áfrica"):
                    continente = "África"
                elif continente.lower() in ("oceania", "oceanía"):
                    continente = "Oceanía"
                else:
                    continente = continente.capitalize()
                #agregar pais    
                resultado = agregar_pais(paises,nombre,poblacion, superficie, continente)

                if resultado:
                    guardar_paises(ruta_csv(), paises)

                    print("Datos guardados correctamente.")
                else:
                    print("No se pudo agregar el país.")
            case "2":
                nombre = pedir_texto("ingrese el nombre del pais que quiere eliminar:   ")
                resultado = eliminar_pais(paises, nombre)
                if resultado:
                    guardar_paises(ruta_csv(),paises)
                    
                
            case "3":
                 nombre = pedir_texto("Ingrese el nombre del país que desea modificar: ")
                 poblacion_actualizada =pedir_entero_positivo("Ingrese la nueva población: ")
                 superficie_actualizada = pedir_entero_positivo("Ingrese la nueva superficie: ")

                 resultado = modificar_pais(paises, nombre, poblacion_actualizada, superficie_actualizada)
                 if resultado:
                     guardar_paises(ruta_csv(), paises)
                     print("País modificado correctamente.")
                 else:
                     print("ERROR: No se pudo modificar el país.")
            case "4":
                 busqueda = pedir_texto("Ingrese el nombre del pais que quiere consultar:   ")
                 resultado = buscar_paises(paises, busqueda)

                 if not resultado:
                    print("No se encontraron países.")

                 else:
                    for pais in resultado:
                        print("------------------------------")
                        print(f"Nombre: {pais['nombre']}")
                        print(f"Población: {pais['poblacion']}")
                        print(f"Superficie: {pais['superficie']} km²")
                        print(f"Continente: {pais['continente']}")

            case "5":
                menu_filtros(paises)

            case "6":
                menu_ordenamientos(paises)
            case "7":
                 menu_estadisticas(paises)
            case "8":
                print("Finalizando programa...")
                break
            case _:
                print("Opción inválida")
####################################################################
#Verificadores
def pedir_texto(mensaje):
    #se repite la solicitud hasta recibir un dato valido
    while True:
        #strip() elimina espacios innecesarios
        texto = input(mensaje).strip()
        #imprime un error si se ingresa un numbre vacio
        if texto == "":
            print("ERROR: El campo no puede estar vacío.")
        else:
            return texto
def pedir_entero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero <= 0:
                print("ERROR: El número debe ser mayor a cero.")
            else:
                return numero

        except ValueError:
            print("ERROR: Debe ingresar un número entero.")

####################################################################
# carga de datos
def cargar_datos_iniciales():
    ruta = ruta_csv ()
    paises = cargar_paises(ruta)
    
    if paises is None:
        print("No se pudieron cargar los datos iniciales.")
        return None

    return paises
def ruta_csv ():
    ruta = os.path.join(os.path.dirname(__file__), "datos", "paises.csv")
    return ruta
    
    
#evita que main() se ejecute automaticamente si se lo importa
if __name__ == "__main__":
    main()