 

def buscar_paises(paises, busqueda):
    encontrados = []

    for pais in paises:
        if busqueda.lower() in pais["nombre"].lower():
            encontrados.append(pais)

    return encontrados

def agregar_pais(paises, nombre, poblacion, superficie, continente):
    pais = {"nombre":nombre,"poblacion":poblacion,"superficie":superficie, "continente":continente}
    paises.append(pais)