 

def buscar_paises(paises, busqueda):
    encontrados = []

    for pais in paises:
        if busqueda.lower() in pais["nombre"].lower():
            encontrados.append(pais)

    return encontrados

def agregar_pais(paises, nombre, poblacion, superficie, continente):
    nombre = nombre.strip()
    continente = continente.strip()
    if nombre == "":
        print("ERROR: El campo no puede estar vacio")
        return
    if continente == "":
        print("ERROR: El campo no puede estar vacio")    
        return
        
    for pais in paises:
        if nombre.lower() == pais["nombre"].lower():
         print ("ERROR: El pais ya se encuentra registrado ")
         return
    
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
    
    
    pais = {
        "nombre":nombre,
            "poblacion":poblacion,
            "superficie":superficie, 
            "continente":continente
            }
    paises.append(pais)
    print("Pais cargado correctamente!!!")

 
 