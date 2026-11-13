import unicodedata
 ####################################################################
def buscar_paises(paises, busqueda):
#se recorre la lista de paises
    encontrados = []

    for pais in paises:
#Si se encuentra el nombre o una coincidencia parcial, se lo agrega a una lista vacia
#y devuelve la lista al finalizar la ejecucion
        if busqueda.lower() in pais["nombre"].lower():
            encontrados.append(pais)
    return encontrados

####################################################################
def agregar_pais(paises, nombre, poblacion, superficie, continente):
#para poder agregar un pais primero hay que evitar
# que se ingrese un campo vacio, eso se busca aplicando strip() sobre las variables    
    nombre = nombre.strip()
    continente = continente.strip()
#se detecta si la variable esta vacia y se finaliza la ejecucion de la funcion
#en caso de que la condicion sea True
    if nombre == "":
        print("ERROR: El campo no puede estar vacio")
        return
    if continente == "":
        print("ERROR: El campo no puede estar vacio")    
        return
#se recorre la lista de paises buscando coincidencias
# en caso de existir coincidencia la funcion se finaliza  
    for pais in paises:
        if nombre.lower() == pais["nombre"].lower():
         print ("ERROR: El pais ya se encuentra registrado ")
         return
#asegurandonos de que no se ingresaron variables vacias ahora vamos a verificar
# que esos datos puedan convertirse a int y que sean mayores a cero
# finalizando la ejecucion de la funcion cuando no se cumplan estas condiciones 
    try:
        poblacion= int(poblacion)
    except ValueError:
        print("ERROR: El valor de la poblacion debe ser un numero entero")
        return
    if poblacion <= 0:
         print ("ERROR: La poblacion debe ser mayor a cero.")
         return
    
    try:
        superficie = int(superficie)
    except ValueError:
        print("ERROR: El valor de la superficie debe ser un numero entero")
        return
    if superficie <= 0:
        print ("ERROR: La superficie debe ser mayor a cero.")
        return
#se agrega el diccionario creado a la lista
    pais = {
        "nombre":nombre,
            "poblacion":poblacion,
            "superficie":superficie, 
            "continente":continente
            }
    paises.append(pais)
    print("Pais cargado correctamente!!!")
####################################################################
def modificar_pais(paises, nombre, poblacion_actualizada, superficie_actualizada):
    #recorremos el diccionario hasta encontrar una coincidencia  
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
          #De encontrarse, vamos a corroborar que los datos
          #ingresados sean numeros y mayores a 0
            try:
                poblacion_actualizada = int(poblacion_actualizada)
            except ValueError:
                print("ERROR: La poblacion debe ser un numero entero")
                return
            if poblacion_actualizada <= 0:
                print("ERROR: La poblacion debe ser mayor a cero")
                return
            
            try: 
                superficie_actualizada = int(superficie_actualizada)
            except ValueError:
                print ("ERROR: La superficie debe ser un numero entero")
                return
          
            if superficie_actualizada <= 0:
                print ("ERROR: La superficie debe ser mayor a cero")
    #Se actualizan los datos
            pais["poblacion"]= poblacion_actualizada
            pais["superficie"] = superficie_actualizada

            print ("Datos modificados correctamente")
            return
    #De no encontrarse imprime un error    
    print ("ERROR: No se encontro el pais")
####################################################################
#normaliza textos para poder buscar de manera uniforme 
def normalizar_texto (texto):
    #se transforma a minuscula
    texto = texto.lower()
    #normalize va a utilizar el formato NFD para separar letras de tildes
    texto = unicodedata.normalize("NFD", texto)
    #recorre la palabra letra por letra separandolas de las tildes 
    # y agregando las letras a la variable
    texto = "".join (letra for letra in texto if unicodedata.category(letra) != "Mm")
    return texto

def filtrar_por_continente(paises, continente):
    encontrados = []
    #el nombre del continente ingresado se "normaliza"
    continente = normalizar_texto(continente)
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
    match criterio:
        case 1:#nombre   
        case 2:#poblacion
        case 3: #superficie
        case _: 
            return "ERROR: Elija una opcion valida"
     
         
 
    match orden :
        case 1: #A-Z
            lista_ordenada_asc =sorted(paises, key=lambda pais: pais["nombre"], reverse= False)
            return lista_ordenada_asc
        case 2: #Z-A
            lista_ordenada_desc = sorted(paises, key=lambda pais: pais["nombre"], reverse= True)
            return lista_ordenada_desc
        case _: 
            return "Error: Elija opcion 1 o 2" 