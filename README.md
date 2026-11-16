El programa permite registrar nuevos países, modificar información existente, realizar búsquedas, aplicar filtros, ordenar los registros y obtener estadísticas generales.
Funcionalidades

El programa cuenta con las siguientes funcionalidades:

1. Agregar países

Registrar nuevos países.

Validar que los campos no estén vacíos.

Comprobar que no existan países duplicados.

Validar que la población y la superficie sean números enteros positivos.

Validar y estandarizar los nombres de los continentes.

2. Modificar países

Buscar un país registrado.

Actualizar su población.

Actualizar su superficie.

Validar los nuevos valores ingresados.

3. Buscar países

Buscar países por su nombre.

Permitir búsquedas parciales.

No distinguir entre mayúsculas y minúsculas.

4. Filtrar países

Filtrar por continente.

Filtrar por rango de población.

Filtrar por rango de superficie.

5. Ordenar países

Permite ordenar los registros según tres criterios:

Nombre.

Población.

Superficie.

Cada criterio admite orden ascendente y descendente.

6. Estadísticas

Identificar el país con mayor población.

Identificar el país con menor población.

Calcular el promedio de población.

Calcular el promedio de superficie.

Contabilizar la cantidad de países por continente.

Tecnologías utilizadas

Python: lenguaje de programación utilizado para desarrollar la aplicación.

CSV: formato utilizado para almacenar y recuperar los datos.

Módulo csv: permite leer y escribir información en archivos CSV.

Módulo os: utilizado para construir rutas de archivos.


Descripción de los archivos:
main.py
Contiene el menú principal y los submenús de la aplicación.

paises.py
Contiene las funciones para agregar, modificar, buscar, filtrar y ordenar países.

archivos.py
Se encarga de leer y guardar los datos en el archivo CSV.

estadisticas.py
Contiene las funciones encargadas de calcular las estadísticas.

paises.csv
Almacena los registros de los países.

Autor

Proyecto desarrollado como parte de la asignatura Programación 1, correspondiente a la Tecnicatura en Programación.

Estudiante: Tonelli Rivarola Benjamin
Institución: Universida Tecnologica Nacional

Año: 2026