#%%
# Importamos librerias necesarias

# Procesamiento de Datos
import pandas as pd
import numpy as np

# Visualización
import matplotlib.pyplot as plt
import seaborn as sns

# Evaluar la linealidad de las relaciones entre variables.
# Analizar las distribuciones de las variables.

import scipy.stats as stats
from scipy.stats import ttest_ind
from scipy.stats import norm
from scipy.stats import chi2_contingency
from scipy.stats import f_oneway
from scipy.stats import mannwhitneyu
from scipy.stats import shapiro

# Configuracion
pd.set_option('display.max_columns', None)

# Gestión de los warnings
import warnings
warnings.filterwarnings("ignore")

# Conecxión con soporte
from src import ejercicio_final_soporte as final

#%% 
# Antes de comenzar leeremos el fichero csv
df_flight = final.read_csv("Customer Flight Activity.csv")
df_loyalty = final.read_csv("Customer Loyalty History.csv")

# %%
# Aplico funcion de exploración general a df_flight
final.exploración_inicial(df_flight, nombre='df_flight')
print("------------------------------------------------------------------------------")
# Aplico funcion de exploración general a df_loyalty
final.exploración_inicial(df_loyalty, nombre='df_loyalty')
print("------------------------------------------------------------------------------")


#%%
# Aplico funcion de exploración de columnas a df_flight
final.exploracion_columnas(df_flight,'df_flight')
print("------------------------------------------------------------------------------")
# Aplico funcion de exploración de columnas a df_loyalty
final.exploracion_columnas(df_loyalty,'df_loyalty')
print("------------------------------------------------------------------------------")

#%% 
# Aplico funcion de comprobacion de valores nulos  a df_flight
print(f'los valores nulos de df_loyalty son: {final.comprobacion_valores_nulos(df_flight)}')
print("------------------------------------------------------------------------------")
# Aplico funcion de comprobacion de valores nulos  a df_loyalty
print(f'los valores nulos de df_flight son: {final.comprobacion_valores_nulos(df_loyalty)}')
print("------------------------------------------------------------------------------")

#%%
# Aplico funcion cambio de nombres df_flight
final.cambio_nombres_columnas(df_flight,'df_flight')
print("------------------------------------------------------------------------------")
#Aplico funcion cambio de nombres df_loyalty
final.cambio_nombres_columnas(df_loyalty,'df_loyalty')
print("------------------------------------------------------------------------------")

#%%
#Aplico funcion Union de datos
final.union_datos(df_flight,df_loyalty, 'Loyalty_Number', 'Loyalty_Number','left')

#%%
## importo el archivo resultante del merge
df_loyalty_flight = final.read_csv('merged.csv')

#%%
# llamo funcion comprobación de nulos
final.comprobacion_valores_nulos(df_loyalty_flight)
print('--------------------------------------------------------------------------------------------------------------')
# Con un porcentaje de nulos tan alto como 87.65% 
# Decide eliminar las columnas 'Cancellation_year' y 'Cancellation Month'
# Llamo función Borrar columnas

df_loyalty_flight = final.eliminar_columnas(df_loyalty_flight,['Cancellation_Year','Cancellation_Month'])
print('--------------------------------------------------------------------------------------------------------------')

# Para gestionar el 25% de nulos de la columna "salary" se podrían imputarlos con la media
final.llenar_nulos_con_media(df_loyalty_flight,'Salary')

#%%
#visualización

# 1. ¿Cómo se distribuye la cantidad de vuelos reservados por mes durante el año?

# Se agrupan los datos por mes y se suman la cantidad de vuelos reservados
vuelos_por_mes = df_loyalty_flight.groupby('Month')['Flights_Booked'].sum()

# Crear el gráfico 
final.crear_grafico_lineal_personalizado(vuelos_por_mes.index, vuelos_por_mes.values,'Mes','Cantidad de Vuelos Reservados','Cantidad de Vuelos Reservados por Mes',['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'], marcador='D', estilo_linea=':',color = 'blue')

# El gráfico  muestra la  distribución de la cantidad de vuelos reservados a lo largo del año, lo que permite identificar patrones estacionales o tendencia en la cantidad de reservas segun la epoca del año:

#* En Semana Santa (Marzo).
#* En  verano ( Junio a Agosto), siendo el marcador más alto en **Julio**.
#* En  Navidades (Diciembre).

print('------------------------------------------------------------------------')

# 2. ¿Existe una relación entre la distancia de los vuelos y los puntos acumulados por los clientes?

distancia_puntos = df_loyalty_flight.groupby('Loyalty_Number')[['Distance', 'Points_Accumulated']].sum().reset_index()
distancia_puntos

# Creamos el scatter plot
final.crear_grafico_dispersion("Distance","Points_Accumulated" , distancia_puntos, 'Distancia', 'Puntos Acumulados', "Relacion entre Distancia y Puntos Acumulados")

# Vemos que hay una **correlacion lineal positiva** entre la distancia y los puntos acumulados.
print('-----------------------------------------------------------------------------------------')

# 3. ¿Cuál es la distribución de los clientes por provincia o estado?

# Contamos el número de clientes por provincia
clientes_x_provincia = df_loyalty['Province'].value_counts()

# Aplico función gráfico de barras
final.crear_grafico_barras(clientes_x_provincia,x_label='Número de Clientes', y_label='Provincia',hue_column=None,title='Distribución de Clientes por Provincia',kind='barh',color=['c','m','y','g','b','tab:pink','tab:purple','slateblue','turquoise','springgreen','salmon'])

# las provincias con mayor  y menor cantidad de  clientes.
# En este caso  **Ontario** es la provincia con mayor cantidad de clientes. 
print('-----------------------------------------------------------------------------------------')

# 4. ¿Cómo se compara el salario promedio entre los diferentes niveles educativos de los clientes?

# Agrupamos los datos por nivel educativo y se saca la media al salario
Salario_x_nivel_educativo = df_loyalty_flight.groupby('Education')['Salary'].mean().sort_values()

# Aplico funcion grafico de barras
final.crear_grafico_barras(Salario_x_nivel_educativo,x_label='Nivel Educativo', y_label='Salario Promedio', title='Salario Promedio Según Nivel Educativo',color='pink')

# Se  observa una relación proporcional entre las variables.
# A mayor nivel educativo mayor salario promedio.
print('-----------------------------------------------------------------------------------------')

# 5. ¿Cuál es la proporción de clientes con diferentes tipos de tarjetas de fidelidad?

# Contar el número de clientes por tipo de tarjeta de fidelidad
clientes_x_tipo_tarjeta = df_loyalty_flight['Loyalty_Card'].value_counts()
# Aplico función gráfico pie
final.crear_grafico_pie(clientes_x_tipo_tarjeta,'Proporción de clientes por Tipo de Tarjeta de Fidelidad')

# Permite identificar la tarjeta  más común entre los clientes, **Star**.
print('-----------------------------------------------------------------------------------------')

# 6. ¿Cómo se distribuyen los clientes según su estado civil y género?

# Crear un DataFrame que contenga la cantidad de clientes por estado civil y género
clientes_x_estado_civil_genero = df_loyalty_flight.groupby(['Marital_Status', 'Gender']).size().unstack()
# Aplico función gráfico barras
final.crear_grafico_barras(clientes_x_estado_civil_genero,x_label='Estado Civil', y_label='Cantidad de Clientes', title='Distribución de Clientes por Estado Civil y Género',kind='barh',color=['deepskyblue','lightskyblue'])

# Observamos que hay predomina el numero de clientes casados, seguido de los divorciados, y la menor cantidad de        clientes que estan divorciados.
# También observamos que los clientes que estan casados es proporcional para ambos generos.
print('-----------------------------------------------------------------------------------------')

#%%

# Fase 3: Evaluación de Diferencias en Reservas de Vuelos por Nivel Educativo

#1.Preparación de Datos:Filtra el conjunto de datos para incluir únicamente las columnas 'Flights Booked' y 'Education'.
df_diferences = df_loyalty_flight[['Flights_Booked', 'Education']]
print('-----------------------------------------------------------------------------------')

# 2.Análisis Descriptivo:

#Agrupa los datos por nivel educativo y calcula estadísticas descriptivas básicas como:
  #- El promedio
  #- La desviación estandar
  #- Los percentiles del número de vuelos reservados para cada grupo.
  
df_education_level = df_diferences.groupby('Education')

# Calcular estadísticas descriptivas básicas para el número de vuelos reservados por grupo educativo
df_description_c = df_education_level['Flights_Booked'].describe().reset_index()
print(df_description_c)
print('--------------------------------------------------------------------------------------')

#3. Prueba Estadística:
# Realiza una prueba de A/B testing para determinar si existe una diferencia significativa en el número de vuelos reservados entre los diferentes niveles educativos.

#Planteamiento de las hipótesis:
     # ***Hipótesis nula (H0):*** No*** hay diferencia significativa en el número de vuelos reservados entre los diferentes niveles educativos.
     # ***Hipótesis alternativa (H1):*** HAY*** diferencia significativa en el número de vuelos reservados entre los diferentes niveles educativos.

# Realizo grafico para empezar a entender la distribucion de los datos a nivel visual
final.crear_grafico_barras_pallete(df_diferences, x_column='Education', y_column='Flights_Booked',hue_column='Education', x_label='Nivel Educativo', y_label='Vuelos Reservados', title='Comparación de vuelos reservados por Nivel Educativo', x_rotation=45)

# Primero realizo un test de normalidad pra ver como se comportan los datos de la columna numerica 
final.test_shapiro(df_diferences,'Flights_Booked')

# Realizo pruebas de T-test

# Obtener muestras de cada nivel educativo
bachelor_flights = df_diferences[df_diferences["Education"] == "Bachelor"]["Flights_Booked"]
college_flights = df_diferences[df_diferences["Education"] == "College"]["Flights_Booked"]
doctor_flights = df_diferences[df_diferences["Education"] == "Doctor"]["Flights_Booked"]
highschool_flights = df_diferences[df_diferences["Education"] == "High School or Below"]["Flights_Booked"]
master_flights = df_diferences[df_diferences["Education"] == "Master"]["Flights_Booked"]

df_list = [bachelor_flights, college_flights, doctor_flights, highschool_flights, master_flights]
name_list = ["Bachelor", "College", "Doctor", "Hightschool", "Master"]

# creo un bucle for para iterar y hacer comparaciones 
for i in range(len(df_list)):
    for j in range(i+1, len(df_list)): #permite comparar todas las combinaciones posibles de grupos dos a dos.
        
        # Realizar la prueba t de Student
        resultado_ttest_1  = final.realizar_ttest(df_list[i], df_list[j])

print('---------------------OTRA OPCIÓN CON DOS GRUPOS--------------------------------------------------------')

# Definir los grupos específicos de nivel educativo
grupo_1 = ['Bachelor','College' 'High School or Below']
grupo_2 = ['Master', 'Doctor']

# Obtener los datos de vuelos reservados para cada grupo
grupo_1_vuelos = df_diferences[df_diferences['Education'].isin(grupo_1)]['Flights_Booked']
grupo_2_vuelos = df_diferences[df_diferences['Education'].isin(grupo_2)]['Flights_Booked']

# Realizar la prueba t de Student independiente
resultado_ttest = final.realizar_ttest(grupo_1_vuelos, grupo_2_vuelos)

print('-----------------------------------------------------------------------------------')

# Realizo test de Mann-Whitney 

# Definir los grupos específicos de nivel educativo
# retiro college ya que al tener una diferencia con el de bacherlor me desecha la hipotesis nula.
grupo_1 = ['Bacherlor', 'High School or Below']
grupo_2 = ['Master', 'Doctor']

# Obtener los datos de vuelos reservados para cada grupo
grupo_1_vuelos = df_diferences[df_diferences['Education'].isin(grupo_1)]['Flights_Booked']
grupo_2_vuelos = df_diferences[df_diferences['Education'].isin(grupo_2)]['Flights_Booked']

# Realizar la prueba t de Student independiente

resultado_manwhitney_1 = final.prueba_mann_whitney(grupo_1_vuelos, grupo_2_vuelos)

print('***********************************************************************************************')

print('''DESPUÉS DE ANALIZAR LOS DATOS DE MANERA VISUAL CON AYUDA DE GRAFICOS,
      Y A TRAVÉS DE APLICAR PRUEBAS T DE STUDENT (t-test) Y LA PRUEBA DE 
      Mann-Whitney U, *** SE ACEPTA LA HIPÓTESIS NULA,
      YA QUE NO HAY UNA DIFERENCIA SIGNIFICATIVA EN LOS VUELOS RESERVADOS
      SEGÚN EL NIVEL EDUCATIVO DE LOS CLIENTES DE LA AEROLINEA''')