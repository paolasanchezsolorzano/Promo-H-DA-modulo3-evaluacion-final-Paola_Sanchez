## Ejercicio Final Módulo 3

#### Este ejercicio cuenta con tres fases en las que se utilizaran herramientas de exploración, limpieza, visualización y analisis de datos 

______________________________________________________________________________________________________________________________________________________________

### Fase 1: Exploración y Limpieza


1.**Exploración Inicial:** 🔎

* Realiza una exploración inicial de los datos para identificar posibles problemas,como valores nulos, atípicos o datos faltantes en las columnas relevantes.
* Utiliza funciones de Pandas para obtener información sobre la estructura de los datos, la presencia de valores nulos y estadísticas básicas de las columnas 
  involucradas.
* Une los dos conjuntos de datos de la forma más eficiente.

2. **Limpieza de Datos:** 🧹
  
* Elimina o trata los valores nulos, si los hay, en las columnas clave para asegurar que los datos estén completos.
* Verifica la consistencia y corrección de los datos para asegurarte de que los datos se presenten de forma coherente.
* Realiza cualquier ajuste o conversión necesaria en las columnas (por ejemplo, cambiar tipos de datos) para garantizar la adecuación de los datos para el 
  análisis estadístico.

### Fase 2: Visualización 📊

**Herramientas de visualización**
  
Usando las herramientas de visualización que has aprendido durante este módulo, contesta a las  siguientes gráficas usando la mejor gráfica que consideres:
  
|                 |                                                         |
| ----------------|---------------------------------------------------------|
|3.| ¿Cómo se distribuye la cantidad de vuelos reservados por mes durante el año?|
|4.| ¿Existe una relación entre la distancia de los vuelos y los puntos acumulados por los clientes?|
|5.|¿Cuál es la distribución de los clientes por provincia o estado?|
|6.|¿Cómo se compara el salario promedio entre los diferentes niveles educativos de los clientes?|
|7.| ¿Cuál es la proporción de clientes con diferentes tipos de tarjetas de fidelidad?|
|8.|¿Cómo se distribuyen los clientes según su estado civil y género?|



### Fase 3: Evaluación de Diferencias en Reservas de Vuelos por Nivel Educativo 🔬

**Objetivo del Ejercicio**

Utilizando un conjunto de datos que hemos compartido, se busca evaluar si existen diferencias significativas en el número de vuelos reservados según el nivel educativo de los clientes. Para 
ello, los pasos que deberas seguir son:

|  | Descripción                                                                                                                      |
|--|----------------------------------------------------------------------------------------------------------------------------------|
|9.|  **Preparación de Datos:** Filtra el conjunto de datos para incluir únicamente las columnas relevantes ('Flights Booked' y 'Education'). |
|10.| **Análisis Descriptivo:** Agrupa los datos por nivel educativo y calcula estadísticas descriptivas básicas (como el promedio, la desviación estándar, los percentiles) del número de vuelos reservados para cada grupo. |
|11.| **Prueba Estadística:** Realiza una prueba de A/B testing para determinar si existe una diferencia significativa en el número de vuelos reservados entre los diferentes niveles educativos. |

______________________________________________________________________________________________________________________________________________________________

**Contenido:** 💾

Podras elegir entre reproducir este repositorio en un archivo python o un Jupyter Notebook, según tus preferencias:

* Encontraras un folder con un archivo Jupyter Notebook.
* Encontarras un folder con un archivo Python.
* Funciones para la visualizacion y limpieza de datos.
* Gráficos que te ayudaran a tener una perspectiva visual de los datos contenidos en el DataFrame.
* Encontraras la conclusión final de nuestro A/B Testing.

<details>
  <summary> Procesos 📂</summary>

  
***Exploración Inicial:***

Se realizó una exploración inicial de los datos para identificar posibles problemas, como valores nulos, atípicos o datos faltantes en las columnas relevantes. Se utilizó funciones de Pandas para obtener información sobre la estructura de los datos, la presencia de valores nulos y estadísticas básicas de las columnas involucradas. Se unieron los dos conjuntos de datos de la forma más eficiente posible.

***Limpieza de Datos:***

Se trataron los valores nulos
Se realizaron ajustes o conversiones necesarias en las columnas 

***Gráficas para la visulización:***

* **Barplot:** Gráfico de barras es una representación visual de datos que utiliza barras rectangulares de diferentes longitudes para mostrar la frecuencia, cantidad o distribución de una variable categórica.

* **Pieplot:** Un gráfico de pastel es un tipo de gráfico circular que muestra la proporción de cada categoría en un conjunto de datos. Cada categoría se representa por un sector del círculo y el tamaño del sector corresponde a la proporción de esa categoría en el conjunto de datos.

* **Regplot:**  Gráfico de regresión , muestra la relación entre dos variables numéricas mediante una línea de regresión. Es útil para visualizar la relación entre una variable independiente (eje x) y una variable dependiente (eje y) y para identificar patrones o tendencias en los datos.


***Evaluación de Diferencias en Reservas de Vuelos por Nivel Educativo:***

* **Preparación de Datos:** Se filtraron los datos para incluir únicamente las columnas relevantes: 'Flights Booked' y 'Education'.
* **Análisis Descriptivo:** Se agruparon los datos por nivel educativo y se calcularon estadísticas descriptivas básicas del número de vuelos reservados para cada grupo.
* **Prueba Estadística:** Se llevó a cabo una prueba de A/B testing con T de student para determinar si existe una diferencia significativa en el número de vuelos reservados entre los diferentes niveles educativos.
</details>


#### Librerias que necesitaras 📚

<details><summary>liberias a importar</summary>
  
#### Evaluar las distribuciones de las variables

* **import pandas as pd**
* **import numpy as np**

#### Visualización.

* **import matplotlib.pyplot as plt**
* **import seaborn as sns**

#### Evaluar la linealidad de las relaciones entre variables.
#### Evaluar las distribuciones de las variables.

* **import scipy**

</details>
</details>






    

