from archivos import cargar_paises
paises = cargar_paises("datos/paises.csv")
####################################################################
def pais_mayor_poblacion(paises):
    if not paises:
        return None
    return max(paises, key=lambda pais: pais["poblacion"], default =None )
####################################################################
def pais_menor_poblacion (paises):
    menor_poblacion = min(
        paises,
        key=lambda pais: pais["poblacion"],
        default=None
    )
    return menor_poblacion
####################################################################
def promediador (paises, atributo):
    if not paises:
        return None

    valores = [pais[atributo] for pais in paises]

    promedio = sum(valores) / len(valores)

    return promedio
####################################################################
def paises_x_continente (paises, continente):
    conteo = {}
    for pais in paises:
        continente = pais["continente"]
        if continente in conteo:
            conteo[continente] += 1
        else:
            conteo[continente] = 1
    return conteo
 