import pandas as pd
#import matplotlib.pyplot as plt
import src.conect_database as conect_database

meses_numeros = {'ENE': 1, 'FEB': 2, 'MAR': 3, 'ABR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AGO': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DIC': 12}


def deuda(mes='total'):
    pd.options.mode.copy_on_write = True
    df = conect_database.read_data()

    if mes == 'total':
        df_meses = df.copy()
        meses = len(df_meses['mes_pago'].unique())
        df_meses['monto_pago'] = df_meses.loc[:, 'monto_pago'].astype(float)
        df_meses['precio_pactado'] = df_meses['precio_pactado'].astype(float)
        df_meses = df_meses.pivot_table(index = 'nombre', values = ['monto_pago','precio_pactado'], aggfunc={'precio_pactado': 'first', 'monto_pago':'sum'})
        df_meses['precio_pactado'] = df_meses['precio_pactado'].transform(lambda x: x*meses)
        df_meses['deuda'] = df_meses['precio_pactado'] - df_meses['monto_pago']
        return df_meses
    
    df_meses = df[df['mes_pago']== mes]
    df_meses['monto_pago'] = df_meses.loc[:, 'monto_pago'].astype(float)
    df_meses['precio_pactado'] = df_meses['precio_pactado'].astype(float)
    df_meses = df_meses.pivot_table(index = 'nombre', values = ['monto_pago','precio_pactado'], aggfunc={'precio_pactado': 'first', 'monto_pago':'sum'})
    df_meses['deuda'] = df_meses['precio_pactado'] - df_meses['monto_pago']
    return df_meses

