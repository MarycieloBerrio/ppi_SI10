# Importa las librerías necesarias
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Página para cargar datos y realizar operaciones
st.title('Calculadora de estadísticas de datos')

 # Enlace para descargar un archivo de ejemplo
example_file_path = "https://bit.ly/example_database"
st.write(f"**Ejemplo de archivo CSV:** [Descargar aquí]({example_file_path})")

# Agregar un botón para cargar datos
uploaded_file = st.file_uploader("Cargar archivo CSV", type=["csv"])

if uploaded_file is not None:
    # Cargar datos usando Pandas
    data = pd.read_csv(uploaded_file)

    # Mostrar las primeras filas del conjunto de datos
    st.subheader('Vista previa del conjunto de datos:')
    st.write(data.head())

    # Operaciones estadísticas básicas
    st.subheader('Estadísticas Básicas:')

    # Filtrar columnas numéricas
    numeric_columns = data.select_dtypes(include=[np.number]).columns

    # Permitir al usuario seleccionar una columna solo si hay columnas numéricas
    if len(numeric_columns) > 0:
        selected_column = st.selectbox('Selecciona columna:',
                                       numeric_columns)
        
        st.write(f"**Media:** {np.mean(data[selected_column])}")
        st.write(f"**Mediana:** {np.median(data[selected_column])}")
        st.write(f"**Desviación estándar:** {np.std(data[selected_column])}")
    else:
        st.warning('El conjunto de datos no contiene columnas numéricas.')

    # Visualización (gráfico de dispersión con opciones)
    st.subheader('Visualización:')
    st.write('Selecciona dos columnas para visualizar un gráfico:')
    scatter_x = st.selectbox('Eje X:', numeric_columns)
    scatter_y = st.selectbox('Eje Y:', numeric_columns)

    # Opciones de tipo de gráfico
    chart_type = st.selectbox('Selecciona el tipo de gráfico:',
                              ['Gráfico de dispersión',
                               'Histograma',
                               'Gráfico de Barras'])

    # Opciones de personalización
    if chart_type == 'Gráfico de dispersión':
        color = st.color_picker('Color de la línea', '#1f77b4')
        marker = st.selectbox('Marcador',
                              ['o', 's', '^', 'v', '>', '<', 'D', 'P'])
        line_width = st.slider('Grosor de la línea', 1, 10, 2)

        # Gráfico de dispersión personalizado con Matplotlib
        fig, ax = plt.subplots()
        ax.scatter(data[scatter_x], data[scatter_y],
                   color=color,
                   marker=marker,
                   linewidths=line_width)
        ax.set_xlabel(scatter_x)
        ax.set_ylabel(scatter_y)
        st.pyplot(fig)

    elif chart_type == 'Histograma':
        color = st.color_picker('Color de las barras', '#1f77b4')
        bins = st.slider('Número de Bins', 1, 100, 20)

        # Histograma personalizado con Matplotlib
        plt.hist(data[scatter_x], bins=bins,
                 color=color, alpha=0.7, rwidth=0.85)
        plt.title('Histograma')
        plt.xlabel(scatter_x)
        plt.ylabel('Frecuencia')
        st.pyplot()

    elif chart_type == 'Gráfico de Barras':
        color = st.color_picker('Color de las barras', '#1f77b4')

        # Gráfico de barras personalizado con Matplotlib
        plt.bar(data[scatter_x].value_counts().index,
                data[scatter_x].value_counts(), color=color)
        plt.title('Gráfico de Barras')
        plt.xlabel(scatter_x)
        plt.ylabel('Frecuencia')
        st.pyplot()

else:
    st.info('Por favor, carga un archivo CSV para comenzar.')
