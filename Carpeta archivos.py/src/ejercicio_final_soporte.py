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

#%%
#Funcion lectura de ficheros
def read_csv(nombre_fichero):
    """
    Esta función esta diseñada para leer ficheros CSV 

    Args:
        nombre_fichero: un str

    Returns:
        Devuelve el DataFrame
    """
    df = pd.read_csv(nombre_fichero)
    return df

#%%
#función Exploracion inicial de los datos 
def exploración_inicial(df, nombre='Tu DataFrame'):
    """
    Función diseñada para proporcionar un resumen detallado de un DataFrame:
    
    - Nombre del DataFrame: Muestra el nombre del DataFrame.
    - Información básica del DataFrame: Muestra la información del tipo de datos para cada columna y la cantidad de valores no nulos.
    - Recuento de filas y columnas: Imprime el número de filas y columnas.
    - Valores nulos: Presenta la cantidad de valores nulos en cada columna.
    - Valores duplicados: Indica la cantidad de filas duplicadas en el DataFrame.
    - Estadísticas descriptivas para columnas numéricas.
    - Estadísticas descriptivas para columnas categóricas.
    
    """
    print(f"Proporcionando un resumen detallado de {nombre}:")
    print("---------------------------------------------------")
    print(f"Las tres primeras filas del DataFrame son:\n{df.head(3)}\n")
    print("---------------------------------------------------------------------------------------------------")
    print(f"Las tres últimas filas del DataFrame son:\n{df.tail(3)}\n")
    print("---------------------------------------------------------------------------------------------------")
    print(f"Información del DataFrame:\n{df.info()}\n")
    print("---------------------------------------------------")
    print(f"Número de filas: {df.shape[0]}, Número de columnas: {df.shape[1]}\n")
    print("---------------------------------------------------")
    print(f"Valores nulos dentro del DataFrame:\n{df.isnull().sum()}\n")
    print("---------------------------------------------------")
    print(f"Datos duplicados dentro del DataFrame: {df.duplicated().sum()}\n")
    print("---------------------------------------------------")
    try:
        print(f"Estadísticas descriptivas para columnas numéricas:\n{display(df.describe().T)}\n")        
        print("------------------------------------------------------------------------")
    except:
        print("No hay columnas numéricas en el DataFrame.")

    try:
        print(f"Estadísticas descriptivas para columnas categóricas:\n{display(df.describe(include='object').T)}\n")
        print("--------------------------------------------------")
    except:
        print("No hay columnas de tipo objeto en el DataFrame.")
        
#%%
# Función exploracion de cada una de las columnas del DataFrame
def exploracion_columnas(df, nombre='Tu DataFrame'):
    
    """ Función diseñada para realizar una exploración detallada de cada columna del DataFrame:
    
       - Nombre de la columna
       - Número de datos: Total de datos en la columna.
       - Frecuencia de valores: Frecuencia de cada valor en la columna.
       - Cantidad de valores únicos: Indica cuántos valores únicos hay en la columna.
       - Tipo de datos: Muestra el tipo de datos de la columna.
       - Valores nulos: Imprime la cantidad de valores nulos en la columna.
       - Valores duplicados: Indica la cantidad de valores duplicados en la columna.
       
    """
    
    print(f" ---------{nombre}---------\n")
    
    for columna in df.columns:
        
        print(f"\n----------- ANALIZANDO LA COLUMNA: '{columna.upper()}' -----------")
        print("------------------------------------------------------------------------")
        print(f"Número de registros de  datos: {len(df[columna].to_list())}")
        print("------------------------------------------------------------------------")
        print(f"Frecuencia de valores en la columna:\n{df[columna].value_counts()}")
        print("------------------------------------------------------------------------")
        print(f"Registros de datos únicos en la columna: {len(df[columna].unique())}")
        print("------------------------------------------------------------------------")
        print(f"Tipo de datos de los valores: {df[columna].dtypes}")
        print("------------------------------------------------------------------------")
        print(f"Suma de valores nulos: {df[columna].isnull().sum()}")
        print("------------------------------------------------------------------------")
        print(f"Suma de valores duplicados: {df[columna].duplicated().sum()}")
        print('---------------------------------------------------------------------------')

#%%
# Función comprobación de valores Nulos   
def comprobacion_valores_nulos(df):
    """Tomamos un DF como entrada, y revisamos el % de Nulos por columna
        Filtramos para mostrar el % de nulos en las columnas que los contengan"""
    
    # calculamos el % de nulos por columna
    df_nulos = pd.DataFrame((df.isnull().sum() / df.shape[0]) * 100, columns = ["%_nulos"])
    # filtramos el DataFrame para quedarnos solo con aquellas columnas que tengan nulos
    
    return df_nulos.round(2)[df_nulos["%_nulos"] > 0] 
 
# Función rellenar valores nulos con la media
def llenar_nulos_con_media(df, nombre_columna):
    """
    Rellena los valores NaN en la columna especificada con el valor medio de esa columna.
    
    Args:
        df (pd.DataFrame): El DataFrame.
        nombre_columna (str): Nombre de la columna a rellenar.
    
    Returns:
        pd.DataFrame: El DataFrame actualizado.
    """
    df[nombre_columna].fillna(df[nombre_columna].mean(), inplace=True)
    
    
    return df       

#%%
# Función Cambio de nombres de las columnas
def cambio_nombres_columnas(dataframe, nombre=None):
    """
    Args:
        -dataframe: Recibe el DataFrame al que se aplicará la función.
        -nombre: El nombre asociado al DataFrame (opcional).
    
    Esta función cambia los nombres de las columnas del DataFrame.
    Recibimos un mensaje de confirmación con el nombre del DataFrame y los nuevos nombres de las columnas.
    """

    if nombre is None:
        nombre = 'Tu DataFrame'
    dataframe.columns = [col.title().strip().replace(" ", "_") for col in dataframe.columns]
    print(f"Los nombres de las columnas en  {nombre} han sido actualizados a \n{list(dataframe.columns)}\n")
    
#%%
# Función  Union de dos Dataframes
def union_datos(df1, df2, col_union_left, col_union_right, union_type="left"):
    """
        Combina dos DataFrames y guarda el resultado en un archivo CSV.

        Args:
        - df1: DataFrame izquierdo.
        - df2: DataFrame derecho.
        - col_union_left: Nombre de la columna en el DataFrame izquierdo para la combinación.
        - col_union_right: Nombre de la columna en el DataFrame derecho para la combinación.
        - Union_type: Tipo de combinación a realizar (por defecto es "left").
    """
    try:
        df_merged = df1.merge(df2, left_on=col_union_left, right_on=col_union_right, how= union_type)
        df_merged.to_csv('merged.csv')
        return df_merged
    except Exception:
        
        return None

#%% 
# Función borrar columnas
def eliminar_columnas(df, columns_to_drop):
     """
        Remueve las columnas especificadas de un DataFrame.
    
        Args:
        df (pd.DataFrame): El DataFrame original.
        columns_to_drop (list): lista de columnas a eliminar.
    
        Returns:
            pd.DataFrame: Actualiza el DataFrame sin las columnas que especificamos.
    """
     return df.drop(columns_to_drop, axis=1)
 
#%%
# Funciones para la visualizacion de los datos

# Función Gráfico lineal
def crear_grafico_lineal_personalizado(x_valores, y_valores, etiqueta_x, etiqueta_y, titulo, etiquetas_eje_x=None, marcador='D', estilo_linea=':', color='blue'):
    """
    Crea un gráfico de líneas personalizable.

    Args:
        x_valores : Valores del eje x.
        y_valores : Valores del eje y.
        x_lavel (str): Etiqueta para el eje x.
        y_label (str): Etiqueta para el eje y.
        titulo (str): Título para el gráfico.
        
        marker (str): Estilo de marcador (por defecto: 'D').
        linestyle (str): Estilo de línea (por defecto: ':').
        color (str): Color de la línea (por defecto: 'blue').
        ______________________________________Opcional_____________________________________
        xticks (lista o None): Etiquetas personalizadas para las marcas del eje x (opcional).

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x_valores, y_valores, marker=marcador, linestyle=estilo_linea, color=color)

    # Personalizar etiquetas de los ejes y agregar un título
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)

    if etiquetas_eje_x:
        plt.xticks(range(1, len(etiquetas_eje_x) + 1), etiquetas_eje_x)

    plt.grid(True)
    plt.show()

#Función Gráfico de Disperción

def crear_grafico_dispersion(x_col, y_col, datos, etiqueta_x, etiqueta_y, titulo):
    """
    Crea un gráfico de dispersión con una línea de regresión.

    Args:
        x_col (str): Nombre de la columna para el eje x.
        y_col (str): Nombre de la columna para el eje y.
        datos (pd.DataFrame): DataFrame que contiene los datos relevantes.
        etiqueta_x (str): Etiqueta para el eje x.
        etiqueta_y (str): Etiqueta para el eje y.
        titulo (str): Título para el gráfico.

    Returns:
        None
    """
    # Configurar el estilo de Seaborn (opcional)
    sns.set_style('darkgrid')
    sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})

    # Crear un gráfico de dispersión con línea de regresión
    sns.regplot(x=x_col, y=y_col, data=datos)

    # Personalizar etiquetas de los ejes y agregar un título
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    plt.title(titulo)
    plt.show()
    
# Función crear gráfico pie
def crear_grafico_pie(dataframe,title):
    """
    Crea un gráfico de pastel utilizando los datos de un DataFrame.

    Args:
        dataframe (pandas.DataFrame): DataFrame con los datos.
        column_name (str): Nombre de la columna con los valores para el gráfico de pastel.
        colors (list, optional): Lista de colores para las secciones del pastel.
        explode (list, optional): Lista de valores para resaltar secciones del pastel.

    Returns:
        None
    """
    plt.figure(figsize=(6, 6))
    plt.pie(dataframe, labels=dataframe.index, autopct='%1.1f%%', startangle=140,
            colors=['c','m','b'], explode=( 0.05 ,0, 0.08) , textprops={'color': 'black'})
    plt.title(title, color="black")
    plt.axis('equal')  # Aspecto igual para asegurar que el pastel se dibuje como un círculo
    plt.legend(loc='lower right')  # Añadir leyenda
    plt.show()
    

# Función Gráfico de barras
def crear_grafico_barras(dataframe,x_column = None, y_column= None,x_label=None, y_label=None,hue_column=None,title=None,kind='bar',color=['b','c']):
    """
    Crea un gráfico de barras apiladas utilizando los datos de un DataFrame.

    Args:
        dataframe (pandas.DataFrame): DataFrame con los datos.
        x_column(str, opcional):columna eje x
        y_column(str,opcional):columna eje y
        x_label(str): poner etiqueta del eje x
        y_label(str): poner etiqueta del eje x
        title (str)_titulo del gráfico
        kind(str): para especificar el tipo de gráfico que deseas crear.Default bar
        color(list, optional): colores para las barras. Si no se proporciona, se usarán colores predeterminados.

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    dataframe.plot(x=x_column, y=y_column,kind=kind, color= color)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()
    
#Función Gráfico de Barras pallete
def crear_grafico_barras_pallete(datos, x_column, y_column, hue_column=None,figsize=(10, 6), x_label=None, y_label=None, title=None, x_rotation=0):
    """
    Crea un gráfico de barras personalizado.

    Args:
        -  datos (pd.DataFrame): DataFrame con los datos.
        -  x_column (str): Nombre de la columna para el eje x.
        -  y_column (str): Nombre de la columna para el eje y.
       
        ___________________________ parametros opcionales_______________________________________________________________________
        
        -  hue_column (str): Nombre de la columna para el agrupamiento por color (si es necesario). Default: None.
        -  palette: (str) parámetro  para el color. Default = 'set2'
        -  figsize (tuple): Tamaño de la figura (ancho x alto). Default: (10, 6).
        -  x_label (str): Etiqueta para el eje x. Default: None.
        -  y_label (str): Etiqueta para el eje y. Default: None.
        -  title (str): Título del gráfico. Default: None.
        -  x_rotation (int): Ángulo de rotación de las etiquetas del eje x. Default = 0.

    """
    plt.figure(figsize=figsize)

    sns.barplot(x=x_column, y=y_column, data=datos, hue=hue_column, palette='Set2')

    if x_label:
        plt.xlabel(x_label)
    if y_label:
        plt.ylabel(y_label)
    if title:
        plt.title(title)

    plt.xticks(rotation=x_rotation)
    plt.show()

#%%   
# Función Test de normalidad
def test_shapiro(dataframe, columna):
    """
    Evalúa la normalidad de una columna de datos de un DataFrame utilizando la prueba de Shapiro-Wilk.

    Parámetros:
        dataframe (DataFrame): El DataFrame que contiene los datos.
        columna (str): El nombre de la columna en el DataFrame que se va a evaluar para la normalidad.

    Returns:
        None: Imprime un mensaje indicando si los datos siguen o no una distribución normal.
    """

    statistic, p_value = stats.shapiro(dataframe[columna])
    if p_value > 0.05:
        print(f"Para la columna {columna} los datos siguen una distribución normal.")
    else:
        print(f"Para la columna {columna} los datos no siguen una distribución normal.")     
#%%
# función Test t-Student

def realizar_ttest(grupo_1, grupo_2):
    """
    Realiza el test t de Student independiente entre dos grupos.

    Args:
        grupo_1 : Datos del primer grupo.
        grupo_2 : Datos del segundo grupo.
        equal_var : Controla si se asume igualdad o no igualdad de las varianzas entre los dos grupos. Default = False
        

    Returns:
        str: Resultado e interpretación del test.
    """
    resultado_ttest = ttest_ind(grupo_1, grupo_2,equal_var=False)

    if resultado_ttest.pvalue < 0.05:
        return print("Rechazamos la hipótesis nula y concluimos que *** HAY *** una diferencia significativa entre los grupos.")
    
    else:
        return print("Aceptamos la hipótesis nula y concluimos que *** No *** hay una diferencia significativa  entre los grupos.") 

# Función prueba de Mann-Whitney U
def prueba_mann_whitney(grupo_1, grupo_2):
    """
    Realiza la prueba de Mann-Whitney U entre dos grupos.

    Args:
        grupo_1 : Datos del primer grupo.
        grupo_2 : Datos del segundo grupo.

    Returns:
        str: Resultado e interpretación de la prueba.
    """
    resultado = mannwhitneyu(grupo_1, grupo_2)

    if resultado.pvalue < 0.05:
        return print("Rechazamos la hipótesis nula y concluimos que *** HAY *** una diferencia significativa entre los grupos.")
    
    else:
        return print("Aceptamos la hipótesis nula y concluimos que *** No *** hay una diferencia significativa  entre los grupos.")          

    
# %%
