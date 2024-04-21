import src.dataframes as dataframes
import matplotlib.pyplot as plt

def img_deuda(mes='total'):
    titulo = [ 'DEUDA TOTAL' if mes=='total' else f'DEUDA {mes}']
    df_meses = dataframes.deuda(mes)
    df_meses = df_meses[df_meses['deuda'] != 0]
    ancho_maximo = max(df_meses['deuda'])

    fig = plt.figure(figsize=(10,4))
    fig.set_facecolor('#f0f0f0')
    bars =plt.barh(df_meses.index,df_meses['deuda'], height=0.8)
    plt.title(titulo[0],fontsize=18, fontfamily='serif',  fontweight='bold', x = 0.4)
    plt.xlabel('Deuda en dólares', fontsize=10, fontfamily='serif')
    for bar in bars:
        ancho = bar.get_width()
        plt.text(ancho+(ancho_maximo/30), bar.get_y()+bar.get_height() / 2, int(round(ancho, 1)), ha = 'center', fontsize = 13)
    plt.xlim(0,ancho_maximo + (ancho_maximo/10))
    plt.savefig(f'imagenes\img_deuda_{mes}.png', bbox_inches='tight', dpi = 300)
    plt.close()