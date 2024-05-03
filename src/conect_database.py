import pandas as pd
import psycopg2
import streamlit as st

@st.cache_data
def read_data():
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='root',
            database='arriendos',
            port='5432'
        )  # type: ignore
        print('Conexión exitosa')
        cur = conn.cursor()
        sql = '''select u.nombre, u.fecha_ingreso, u.precio_pactado, d.departamento, d.id_departamento, 
                p.mes_pago, p.year_pago, p.monto_pago, p.fecha_pago from usuarios u
                join departamentos d on d.id_usuario = u.id_usuario
                join Pagos p on u.id_usuario = p.id_usuario;'''
        cur.execute(sql)
        datos = cur.fetchall()
        columnas = [descripcion[0] for descripcion in cur.description]
        cur.close()
        conn.close()
        df = pd.DataFrame(datos, columns=columnas)
    except Exception as ex:
        print(f'Error: {ex}')
    else:
        print('Cerrando sesión')
        
    return df