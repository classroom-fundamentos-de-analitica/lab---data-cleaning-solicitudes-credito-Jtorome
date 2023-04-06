"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df['sexo'] = df['sexo'].apply(str.lower)
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].apply(lambda x: x.lower() if type(x) == str else x)
    df['idea_negocio'] = df['idea_negocio'].apply(lambda x: x.lower().replace('_', ' ').replace('-', ' ') if type(x) == str else x)
    df['barrio'] = df['barrio'].apply(lambda x: x.lower().replace('_', ' ').replace('-', ' ') if type(x) == str else x)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], format='%d/%m/%Y', errors='coerce').fillna(
        pd.to_datetime(df['fecha_de_beneficio'], format='%Y/%m/%d', errors='coerce')
    )
    df['monto_del_credito'] = df['monto_del_credito'].apply(lambda x: x.replace('$', '').strip().replace(',', '').replace('.00', '') if type(x) == str else x)
    df['línea_credito'] = df['línea_credito'].apply(lambda x: x.lower().replace('_', ' ').replace('-', ' ') if type(x) == str else x)
    return df
