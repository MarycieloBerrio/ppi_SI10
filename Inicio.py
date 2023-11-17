# Importa las librerías necesarias
import streamlit as st

# Configura el título y el favicon de la página
st.set_page_config(
    page_title="Data Insight",
    page_icon="📊​​"
)

# Pagina de inicio
st.title('Data Insight')
st.write('Bienvenido a Data Insight, una calculadora de \
         estadísticas de datos. Esta aplicación te permite\
         realizar operaciones estadísticas básicas en tus \
         conjuntos de datos.')

st.header('Instrucciones de uso:')
st.write('1. Haz clic en el botón "Cargar Datos" para cargar \
         tu conjunto de datos en formato CSV.')
st.write('2. Explora las estadísticas básicas y visualizaciones\
          generadas automáticamente.')
st.write('3. Utiliza las opciones de personalización.')

st.header('Información de Contacto:')
st.write('Desarrollado por Marycielo Berrio')
st.write('Correo Electrónico: mberrioz@unal.edu.co')
st.write('Colaborador: ChatGPT')
