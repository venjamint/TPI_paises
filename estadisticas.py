
####################################################################
def pais_mayor_poblacion(paises):
    #en caso de que la lista paises se encuentre vacia
    if not paises:
        return None
    #devuelve el pais con mayor poblacion
    return max(paises, key=lambda pais: pais["poblacion"], default =None )
####################################################################
def pais_menor_poblacion(paises):
    if not paises:
        return None

    return min(paises, key=lambda pais: pais["poblacion"])
####################################################################
def promediador (paises, atributo):
    #en caso de que poblacion o superficie se encuentre vacio
    if not paises:
        return None
    #se recorren los atributos que se quieren promediar y se guardan en 
    #esta variable
    valores = [pais[atributo] for pais in paises]
    #calculo del promedio
    promedio = sum(valores) / len(valores)

    return promedio
####################################################################
def paises_x_continente (paises):

    #se inicia un diccionario vacio donde se iran sumando los conteos
    conteo = {}
    #se recorre cada diccionario en la lista
    for pais in paises:
        #en cada iteracion la variable continente va a guardar el valor
        # de la clave "continente" de cada diccionario
        continente = pais["continente"]
        #si ya esta contada se suma uno a conteo
        if continente in conteo:
            conteo[continente] += 1
        #si no, inicia el contador para ese continente
        else:
            conteo[continente] = 1
    return conteo
