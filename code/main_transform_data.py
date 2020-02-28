'''
Este módulo incluye funciones que se encargan de transformar variables, es decir,
transformaciones en columnas de una base de datos en formato DataFrame de la
paquetería "PANDAS".
'''
import pandas as pd

def to_lowercase(df,cols):
    for col in cols:
        df[col]=df[col].str.lower()
    return df

def remove_special_char(df,col_name):
    '''
    Reemplaza acentos y caracteres especiales de la columna especificada.
    df: dataframe
    col_name: nombre de la columna
    '''
    df[col_name] = df[col_name].str.replace(' ', '_')
    df[col_name] = df[col_name].str.replace('.', '')
    #quita acentos
    df[col_name] = df[col_name].str.replace('á', 'a')
    df[col_name] = df[col_name].str.replace('é', 'e')
    df[col_name] = df[col_name].str.replace('í', 'i')
    df[col_name] = df[col_name].str.replace('ó', 'o')
    df[col_name] = df[col_name].str.replace('ú', 'u')
    df[col_name] = df[col_name].str.replace('ñ', 'n')
    df[col_name] = df[col_name].str.replace('+', '')
    # Para dos casos específicos que se encontraron en las celdas de los municipios

    # Aplica particularmente para el caso analizado
    #df[col_name] = df[col_name].str.replace('la_', '')
    #df[col_name] = df[col_name].str.replace('talpan','tlalpan')
    return df

def switch_type(df, col_name, tipo):
    '''
    Cambiael tipo de una variable en el dataframe
    df: dataframe
    col_name: nombre de la columna
    tipo: tipo de variable al que se quiere convertir la columna
    '''
    if tipo == "numeric":
        df[col_name] = df[col_name].astype('float64')
    elif tipo == "string":
        df[col_name] = df[col_name].astype('str')
    elif tipo == "category":
        df[col_name] = df[col_name].astype('category')
    elif tipo == "int":
        df[col_name] = df[col_name].astype('int64')
    else:
        print("Variable de tipo no especificadosdsdsd")
    return df
