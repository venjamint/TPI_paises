import unicodedata
 ####################################################################
def buscar_paises(paises, busqueda):

    encontrados = []
    #quita mayusculas y tildes de un texto para facilitar la busqueda
    busqueda = normalizar_texto(busqueda)
    #se recorre la lista con los paises
    for pais in paises:
    #en cada iteracion el nombre del pais tambien es normalizado 
        nombre = normalizar_texto(pais["nombre"])
    #si hay conincidencia total o parcial la agrega a encontrados[]
        if busqueda in nombre:
            encontrados.append(pais)
    return encontrados
####################################################################
def agregar_pais(paises, nombre, poblacion, superficie, continente):

    # Eliminar espacios innecesarios
    nombre = nombre.strip()
    continente = continente.strip()

    # Validar que los campos de texto no estén vacíos
    if nombre == "":
        print("ERROR: El nombre del país no puede estar vacío.")
        return False

    if continente == "":
        print("ERROR: El continente no puede estar vacío.")
        return False

    # Verificar que el país no esté registrado
    for pais in paises:
        if nombre.casefold() == pais["nombre"].casefold():
            print("ERROR: El país ya se encuentra registrado.")
            return False

    # Crear el nuevo registro
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    # Agregar el país a la lista
    paises.append(nuevo_pais)

    return True
####################################################################
def eliminar_pais(paises, nombre):
     
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            paises.remove(pais)
            print("Pais eliminado exitosamente!!!")
            return True
           
     
    print ("ERROR: No se encontro el pais")
    return False
####################################################################
def modificar_pais (paises, nombre, poblacion_actualizada, superficie_actualizada):
    #recorremos el diccionario hasta encontrar una coincidencia  
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
          #De encontrarse, vamos a corroborar que los datos
          #ingresados sean numeros y mayores a 0
            try:
                poblacion_actualizada = int(poblacion_actualizada)
            except ValueError:
                print("ERROR: La poblacion debe ser un numero entero")
                return False
            if poblacion_actualizada <= 0:
                print("ERROR: La poblacion debe ser mayor a cero")
                return False
            
            try: 
                superficie_actualizada = int(superficie_actualizada)
            except ValueError:
                print ("ERROR: La superficie debe ser un numero entero")
                return False
          
            if superficie_actualizada <= 0:
                print ("ERROR: La superficie debe ser mayor a cero")
                return False 
    #Se actualizan los datos
            pais["poblacion"]= poblacion_actualizada
            pais["superficie"] = superficie_actualizada

            print ("Datos modificados correctamente")
            return True
    #De no encontrarse imprime un error    
    print ("ERROR: No se encontro el pais")
    return False
####################################################################
#normaliza textos para poder buscar de manera uniforme 
def normalizar_texto (texto):
    #se transforma a minuscula
    texto = texto.lower()
    #normalize va a utilizar el formato NFD para separar letras de tildes
    texto = unicodedata.normalize("NFD", texto)
    #recorre la palabra letra por letra separandolas de las tildes 
    # y agregando las letras a la variable
    texto = "".join (letra for letra in texto if unicodedata.category(letra) != "Mn")

    return texto

####################################################################
def filtrar_por_continente(paises, continente):
    encontrados = []
    #el nombre del continente ingresado se "normaliza"
    continente = normalizar_texto(continente)
    if not continente:
         print ("ERROR no se puede ingresar un campo vacio")
         return encontrados
    #se recorre la lista paises "normalizando" el valor que contiene "continente"
    for pais in paises:
        continente_pais = normalizar_texto(pais["continente"])
    #si se encuentra una coincidencia se agrega a la lista
        if continente_pais == continente:
            encontrados.append(pais)
     
    return encontrados
####################################################################
def filtrar_por_poblacion (paises, minimo, maximo):
    encontrados = []
    try:
        minimo = int(minimo)
        maximo = int(maximo)
    except ValueError:
        print ("ERROR: Los limites deben ser numeros enteros")
        return encontrados
    if minimo < 0 or maximo < 0:
        print ("ERROR: Los limite no pueden ser negativos") 
        return encontrados
    if minimo > maximo:
        print("ERROR: El minimo no puede ser mayor al maximo.")
        return encontrados

    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            encontrados.append(pais)
    return encontrados
####################################################################
def filtrar_por_superficie (paises, minimo, maximo):
    encontrados = []
    try:
        minimo = int(minimo)
        maximo = int(maximo)
    except ValueError:
        print ("ERROR: Los limites deben ser numeros enteros")
        return encontrados
    if minimo < 0 or maximo < 0:
        print ("ERROR: Los limite no pueden ser negativos") 
        return encontrados
    if minimo > maximo:
        print("ERROR: El minimo no puede ser mayor al maximo.")
        return encontrados

    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            encontrados.append(pais)
    return encontrados
####################################################################
def ordenar(paises,criterio, orden):
    #se encarga de ordenar los diccionarios segun el caso seleccionador
    match criterio:
        case 1:#nombre   
            clave =  lambda pais:pais["nombre"]
        case 2:#poblacion
            clave  =   lambda pais:pais["poblacion"]
        case 3: #superficie
            clave  =    lambda pais:pais["superficie"]
        case _:    
            print("ERROR: Elija una opcion valida")
            return []

         
    #en el orden seleccionado 
    match orden :
        case 1: #A-Z
            lista_ordenada= sorted(paises, key=clave, reverse= False)
            return lista_ordenada 
        case 2: #Z-A
            lista_ordenada= sorted(paises, key=clave, reverse= True)
            return lista_ordenada 
        case _: 
             
            print("Error: Elija opcion 1 o 2")
            return [] 
####################################################################      
def mostrar_paises(resultado):

    if not resultado:
        print("No se encontraron países.")
        return False

    for pais in resultado:
        print("------------------------------")
        print(f"Nombre: {pais['nombre']}")
        print(f"Población: {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']} km²")
        print(f"Continente: {pais['continente']}")
        
