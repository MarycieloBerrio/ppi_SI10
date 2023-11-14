import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Análisis de Datos con Streamlit", layout="wide")

# Título de la aplicación
st.title("Análisis de Datos con Numpy, Pandas y Matplotlib")

# Sección de carga de datos
uploaded_file = st.file_uploader("Cargar archivo CSV o Excel", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Cargar datos con Pandas
    df = pd.read_csv(uploaded_file)  # Puedes cambiar a pd.read_excel() si es un archivo Excel

    # Mostrar el conjunto de datos
    st.subheader("Conjunto de Datos")
    st.write(df)

    # Manipulación de datos con Numpy y Pandas
    # (Aquí puedes agregar las manipulaciones según tus necesidades)

    # Cálculos estadísticos
    st.subheader("Cálculos Estadísticos")
    st.write("Media:", df.mean())
    st.write("Mediana:", df.median())
    st.write("Desviación Estándar:", df.std())
    st.write("Mínimo:", df.min())
    st.write("Máximo:", df.max())

    # Visualización de datos con Matplotlib
    st.subheader("Visualización de Datos")

    # Ejemplo de gráfico de barras
    st.bar_chart(df)

    # (Puedes agregar más tipos de gráficos según sea necesario)

    # Nota: Asegúrate de cerrar el gráfico para evitar superposiciones
    plt.close()

    # Presentación de resultados en la interfaz de usuario
    st.subheader("Resultados")

    # (Aquí puedes presentar más resultados según tus necesidades)
