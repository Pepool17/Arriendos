import src.create_image as create_image
import src.generar_informe as generar_informe
#import src.conect_database as conect_database
#import dataframes

if __name__ == '__main__':
    create_image.img_deuda('ENE')
    generar_informe.informe()