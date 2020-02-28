
from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from IPython.display import display  # para imprimir los dataframes
# TABLA DE RESUMEN GENERAL
# ----------------------------------------
def tipos_variables(df):
    variable_name = []
    tipos_variable = []
    for col in df.columns:
        if df[col].dtypes == ("float64" or "int64"):
            tipos_variable.append("numerica")
            variable_name.append(col)
        elif df[col].dtypes == ("object"):
            tipos_variable.append("categerica")
            variable_name.append(col)
        else:
        # las variables anio, bimestre y gif son reconocidas como int64 pero no asignadas
            tipos_variable.append("otro / numérica")
            variable_name.append(col)

    df_tipos_variables = pd.DataFrame({'variable': variable_name,
                                  'tipo_variable': tipos_variable})
    df_tipos_variables = df_tipos_variables.sort_values(by = "tipo_variable")
    return df_tipos_variables

def resumen_tabla(df):
    '''
    Esta función ayuda a resumir el contenido general del dataframe(df) generando una tabla con:
    número de observaciones
    número de variables
    nombres de las variables
    '''
    nro_obs = df.shape[0]
    nro_vars = df.shape[1]
    nro_missing = sum(df.isna().mean().round(4))*100
    resumen = {'observaciones': [nro_obs], 'variables': [nro_vars], 'faltantes (%)': [nro_missing] }
    df_resumen = pd.DataFrame(data = resumen)
    return df_resumen

def missing_values(df, col):
    '''
    Calcula el número total y e porcentaje de missing values
    '''
    nro_obs = df[col].shape[0]
    porc_missing = df[col].isna().mean().round(4) * 100
    nro_missing = df[col].isna().sum()
    resumen = {'Missing (total)': [nro_missing], "Missing (%)": [porc_missing]}
    df_resumen = pd.DataFrame(data = resumen)
    display(df_resumen)

def normality_stats(df, col):
    '''
    Calcula skewness y kurtosis para una columna de un dataframe
    '''
    skw = df[col].isna().mean().round(4) * 100
    kurt = df[col].isna().sum()
    resumen = {'skewness': [skw], "kurtosis": [kurt]}
    df_resumen = pd.DataFrame(data = resumen)
    display(df_resumen)

# VARIABLES NUMÉRICAS
# Gráficas y reportes para las variables numéricas
# ----------------------------------------
def histograma_plot(df, col):
    # falta incluir missings (totales y proporciones)
    '''
    '''
    q95 = df[col].quantile(0.95)
    q05 = df[col].quantile(0.05)
    test = df[(0 < df[col]) & (df[col] <= q95)]
    sns.distplot(test[col].dropna())
    plt.show()

# VARIABLES CATEGÓRICAS
# Gráficas y reportes para las variables categóricas
# ----------------------------------------
def bar_plot(df, col):
    '''
    gráfico de barras de frecuencia para la variable categórica
    '''
    sns.countplot(y = col, data = df, order = df[col].value_counts().index)
    plt.show()
# ----------------------------------------
# GRÁFICAS GENERALES PARA TODO EL DATASET
# Nota: gráficas tomadas de las plantillas de seaborn
# Grafica de correlaciones generales - Pearson
def remove_columns(df,col_name):
    return df.drop(columns=col_name)


def heatmap_corr_pearson(dataframe):
    '''
    Genera el heatmat de correlaciones entre todas las variables del dataframe en formato pandas
    '''
    sns.set(style="white")
    # remover anio, latitude, longitude, gid

    dataframe = remove_columns(dataframe,"anio")
    dataframe = remove_columns(dataframe,"latitude")
    dataframe = remove_columns(dataframe,"longitude")
    dataframe = remove_columns(dataframe,"gid")

    corr = dataframe.corr(method = "pearson") # se computa la correlación de las variables

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap="YlGnBu", vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

# Grafica de correlaciones generales - Kendall
def heatmap_corr_kendall(dataframe):

    '''
    Genera el heatmat de correlaciones entre todas las variables del dataframe en formato pandas
    '''
    sns.set(style="white")

    dataframe = remove_columns(dataframe,"anio")
    dataframe = remove_columns(dataframe,"latitude")
    dataframe = remove_columns(dataframe,"longitude")
    dataframe = remove_columns(dataframe,"gid")

    corr = dataframe.corr(method = "kendall") # se computa la correlación de las variables

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap="YlGnBu", vmax=.3, center=0,
            square=True, linewidths=.5) #cbar_kws={"shrink": .5}

# Grafica de correlaciones generales - Spearman
def heatmap_corr_spearman(dataframe):

    '''
    Genera el heatmat de correlaciones entre todas las variables del dataframe en formato pandas
    '''
    sns.set(style="white")

    dataframe = remove_columns(dataframe,"anio")
    dataframe = remove_columns(dataframe,"latitude")
    dataframe = remove_columns(dataframe,"longitude")
    dataframe = remove_columns(dataframe,"gid")

    corr = dataframe.corr(method = "spearman") # se computa la correlación de las variables

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))


    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap="YlGnBu", vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

# Gráficas para relacionar categóricas con numéricas
def boxplot_category(x, y, df):
    sns.catplot(x, y,data=df, saturation=.5,kind="bar", aspect=.6)
    plt.show()
def plot_three_cat(x, y, z, df):
    g = sns.catplot(x, y, hue=z, data=df, height=10)
    g = sns.boxplot(x, y, data=df, whis=np.inf)

    # plt.show()
# Adicionales
def df_numerico(df):
    '''
    Genera un dataframe solamente con las variables numéricas.
    Adicionalmente remueve latitude y longitude.
    '''
    df = remove_columns(df,"latitude")
    df = remove_columns(df,"longitude")
    for col in df.columns:
        if df[col].dtypes != ("float64" or "int64"):
            df = remove_columns(df,col)
        else:
            continue

    return df


def df_categorico(df):
    '''
    Genera un dataframe solamente con las variables categñoricas.
    Adicionalmente remueve la variable anio.
    '''
    df = remove_columns(df,"anio")
    for col in df.columns:
        if df[col].dtypes == ("float64" or "int64"):
            df = remove_columns(df,col)
        else:
            continue
    return df
