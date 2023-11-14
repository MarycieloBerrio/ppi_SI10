pip install matplotlib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Análisis de Datos - Cargar Datos y Resumen General")

# Sección para cargar datos
uploaded_file = st.file_uploader("Cargar archivo de datos", type=["csv", "xlsx"])
if uploaded_file is not None:
    # Cargar datos con Pandas
    df = pd.read_csv(uploaded_file)  # Reemplaza con pd.read_excel() si es un archivo Excel

    # Mostrar una tabla con los datos
    st.write("**Conjunto de datos:**")
    st.write(df)

    # Resumen estadístico básico con Pandas
    st.write("**Resumen Estadístico:**")
    st.write(df.describe())

    # Visualización de tendencias con Matplotlib (ejemplo: histograma)
    st.write("**Visualización de Tendencias:**")
    column_to_plot = st.selectbox("Seleccionar columna para visualizar", df.columns)
    plt.hist(df[column_to_plot], bins=30, edgecolor="black")
    st.pyplot()

