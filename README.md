Gestión de Datos de Países

Trabajo Práctico Integrador de Programación 1. Esta aplicación de consola, desarrollada en Python, permite gestionar información de países almacenada en un archivo CSV. El proyecto aplica listas, diccionarios, funciones, estructuras condicionales y repetitivas, búsqueda, filtrado, ordenamiento y estadísticas.

Funcionalidades

Agregar países con nombre, población, superficie y continente. El programa valida los campos ingresados, evita nombres duplicados y requiere valores enteros positivos para población y superficie.

Modificar la población y la superficie de un país.

Buscar países por nombre completo o por coincidencia parcial. La búsqueda ignora mayúsculas y tildes, y solicita un texto no vacío.

Filtrar países por continente, rango de población o rango de superficie.

Ordenar por nombre, población o superficie, en orden ascendente o descendente.

Consultar el país con mayor y menor población, los promedios de población y superficie, y la cantidad de países por continente.

Eliminar países, como opción adicional del sistema.

El programa también controla el formato del encabezado del CSV y los valores numéricos al cargar los datos, y muestra mensajes cuando no encuentra resultados o detecta entradas inválidas.

Datos

Los países se almacenan en datos/paises.csv, con estos campos:

nombre,poblacion,superficie,continente

Ejemplo de registro:

Argentina,47070217,3761274,América

El programa carga los datos al iniciarse y guarda los cambios realizados al agregar, modificar o eliminar países.

Requisitos

Python 3.10 o posterior.

No se requieren bibliotecas externas.

Cómo ejecutar

Desde la carpeta raíz del proyecto, ejecutar:

python main.py

El sistema mostrará un menú en consola. Ingresá el número de la opción deseada y seguí las indicaciones.

Ejemplos de uso

Búsqueda parcial

Entrada:

Seleccione una opción: 4
Ingrese el nombre del pais que quiere consultar: Arg

Salida esperada con el CSV de ejemplo:

Nombre: Argentina
Población: 47070217
Superficie: 3761274 km²
Continente: América

Los valores mostrados dependen del contenido actual de datos/paises.csv.

Búsqueda vacía

Si se deja vacío el texto de búsqueda, el programa solicita un valor válido:

Ingrese el nombre del pais que quiere consultar:
ERROR: El campo no puede estar vacío.

Archivos principales

main.py: menú principal, submenús y coordinación de las operaciones.

paises.py: funciones de gestión, búsqueda, filtrado y ordenamiento.

archivos.py: carga y guardado del archivo CSV.

estadisticas.py: cálculos estadísticos.

datos/paises.csv: conjunto de datos inicial.