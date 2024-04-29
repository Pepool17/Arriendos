import pandas as pd
#import matplotlib.pyplot as plt
import src.conect_database as conect_database


def meses_numeros():
    return {'ENE': 1, 'FEB': 2, 'MAR': 3, 'ABR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AGO': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DIC': 12}


def pagos():
    meses_numeros = meses_numeros()
    df = conect_database.read_data()
    df['mes_numero'] = df['mes_pago'].map(meses_numeros)

    # Crea un dataframe para ver el nombre de los usuarios y sus pagos segun los meses
    pivot_df = df.pivot_table(index=['nombre', 'departamento'], columns='mes_numero', values=['monto_pago', 'fecha_pago'], aggfunc={'monto_pago': 'sum', 'fecha_pago': 'first'})
    pivot_df.columns = pivot_df.columns.swaplevel()
    pivot_df = pivot_df.sort_index(axis=1)

    # Cambia los numeros por el mes
    iniciales_meses = list(map(lambda x: (next(key for key, value in meses_numeros.items() if value == x[0]), x[1]), pivot_df.columns))
    iniciales_meses = list(map(lambda x: (x[0],x[1].replace('fecha_pago', 'fecha')), iniciales_meses))
    iniciales_meses = list(map(lambda x: (x[0],x[1].replace('monto_pago', 'pago')), iniciales_meses))
    pivot_df.columns = pd.MultiIndex.from_tuples(iniciales_meses)
    return pivot_df    


def deuda(mes='total'):
    pd.options.mode.copy_on_write = True
    df = conect_database.read_data()
    df_deuda = df.copy()
    df_deuda['precio_pactado'] = df_deuda['precio_pactado'].astype(float)
    df_deuda['monto_pago'] = df_deuda['monto_pago'].astype(float)
    meses = df_deuda['mes_pago'].unique()
    df_deuda = df_deuda.pivot_table(index=['nombre','precio_pactado','departamento'], columns='mes_pago', values=['monto_pago'], aggfunc={'monto_pago':'sum'})
    df_deuda.columns = df_deuda.columns.swaplevel()
    
    df_deuda = df_deuda.rename(columns={'precio_pactado':'deuda', 'monto_pago': 'pago'})
    df_deuda = df_deuda.fillna(0)

    for elementos in meses:
       df_deuda[(elementos, 'deuda')] = df_deuda.index.get_level_values(1).tolist()
       df_deuda[(elementos, 'deuda')]= df_deuda[(elementos,'deuda' )] - df_deuda[(elementos, 'pago')]

    df_deuda = df_deuda.sort_index(axis=1, ascending=False)

    if mes == 'total':
        deuda_total= df_deuda.loc[:, df_deuda.columns.get_level_values(1) == 'deuda'].sum(axis=1)
        return pd.DataFrame(deuda_total.values, index=[df_deuda.index.get_level_values(2),df_deuda.index.get_level_values(0)], columns=['deuda'])
         
    df_deuda = df_deuda.loc[:,df_deuda.columns.get_level_values(0) == mes]
    pago = df_deuda[(mes,'pago')].tolist()
    deuda = df_deuda[(mes,'deuda')].tolist()
    precio = df_deuda.index.get_level_values(1)
    lista = list(zip(precio,pago,deuda))
    df_deuda = pd.DataFrame(lista, index=[df_deuda.index.get_level_values(2),df_deuda.index.get_level_values(0)], columns=['precio', 'pago', 'deuda'])
    return df_deuda

