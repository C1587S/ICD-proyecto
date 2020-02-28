'''
Este módulo incorpora funciones para limpiar la base de datos de forma general.
Es decir, se realizan transformaciones a todas las columnas del dataframe.
'''

import pandas as pd

def clean_column_names(df, col_names=[]):
    '''
    Cambia nombres de las variables a minúsculas
    '''
    df.columns = [col.lower()  for col in df]
    df.columns = df.columns.str.replace(' ', '_')#espacios por guiones
    return df


def eliminar_col(df, col_name):
    '''
    Elimina columnas específicas del dataframe
    df: dataframe
    col_name: nombre de la columna
    '''
    return df.drop(columns=col_name)

def split_column(df , col_name, new_col_name_1, new_col_name_2, sep = ",", del_col = False):
    '''
    Separa una columna única (col_name) que tienen dos datos alojados simultáneamente en dos columnas
    df: dataframe
    col_name: String, columna que contiene los dos valores
    new_col_name_1: String, columna que va a contener el primer valor (de izquierda a derecha)
    new_col_name_2: String, columna que va a contener el segundo valor (de izquierda a derecha)
    sep: String, caracter por el cual están separados los valores en col_name
    del_col: Boolean, especifica si se quiere eliminar la columna separada
    '''
    df[[new_col_name_1,new_col_name_2]] = df[col_name].str.split(",",expand=True)
    if del_col==True:
        df=df.drop(columns=col_name)
    return df
