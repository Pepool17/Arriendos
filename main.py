import src.generar_informe as generar_informe
import src.conect_database as conect_database

if __name__ == '__main__':
    df = conect_database.read_data()    
    generar_informe.informe(df)

 