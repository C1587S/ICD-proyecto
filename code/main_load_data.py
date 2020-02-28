'''
Este módulo incorpora funciones para cargar la base de datos.
'''
import pandas as pd

def read_data(ruta_data_csv, sep = ";"):
    '''
    Importa archivos CSV que se encuentran de forma local.
    En este momento solo sirve para base con formato CSV
    '''
    df = pd.read_csv(ruta_data_csv, sep= ";")
    return df
