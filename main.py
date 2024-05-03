import src.generar_informe as generar_informe
import src.conect_database as conect_database
import src.dataframes as dataframes
import streamlit as st


def main():    
    df = conect_database.read_data()
    meses = ['TOTAL', 'ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC']
    
    st.title('Arriendos')
    st.subheader("Fecha de pagos")
    df1 = dataframes.pagos(df)
    df1 = df1.set_index(df1.index.get_level_values(1))
    st.write(df1)

    st.subheader("Deudas")
    mes = st.selectbox("Selecciona un mes", meses)
    df2 = dataframes.deuda(df, mes)

    if isinstance(df2, str):
        st.dataframe(df2)

    else:
        df2 = df2.set_index(df2.index.get_level_values(0))
        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(df2)

        with col2:  
            try:
                ruta_img = f'imagenes/img_deuda_{mes}.png'
                st.image(str(ruta_img), use_column_width=True)

            except:
                None
        
    

if __name__ == '__main__':
      
    #generar_informe.informe(df)
    main()
    
    
    

 