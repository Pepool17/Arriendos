import src.dataframes as dataframes
import matplotlib.pyplot as plt
import datetime


def img_deuda(df, mes='total'):
    titulo = [ 'DEUDA TOTAL' if mes=='total' else f'DEUDA {mes}']
    df_meses = dataframes.deuda(df, mes)
    #df_meses = df_meses[df_meses['deuda'] != 0]
    ancho_maximo = max(df_meses['deuda'])

    fig = plt.figure(figsize=(6,5))
    fig.set_facecolor('#f0f0f0')
    bars =plt.barh(df_meses.index.get_level_values(0),df_meses['deuda'], height=0.8)
    plt.title(titulo[0],fontsize=18, fontfamily='serif',  fontweight='bold')
    plt.xlabel('Deuda en dólares', fontsize=10, fontfamily='serif')
    for bar in bars:
        ancho = bar.get_width()
        plt.text(ancho+(ancho_maximo/30), bar.get_y()+bar.get_height() / 2, int(round(ancho, 1)), ha = 'center', fontsize = 13)
    plt.xlim(0,ancho_maximo + (ancho_maximo/10))
    plt.savefig(f'imagenes\img_deuda_{mes}.png', bbox_inches='tight', dpi = 300)
    plt.close()


def consutar_deuda(df):
    import datetime
    fecha_actual = datetime.datetime.now()
    mes_actual = fecha_actual.month

    meses = ['total']
    img_deuda(df)

    meses_numeros = dataframes.meses_num()
    try:
        for mes in meses_numeros.keys():

            if meses_numeros[mes] == mes_actual + 1:
                return meses
            
            df_mes = dataframes.deuda(df, mes)
            if df_mes['deuda'].agg(lambda x: sum(x)) != 0:
                img_deuda(df, mes)
                meses.append(mes)
                
    except KeyError:      
        return meses
    