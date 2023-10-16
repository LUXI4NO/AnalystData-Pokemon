import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página de la aplicación
st.set_page_config(page_title="Análisis de Datos Pokémon", layout="wide")

# Cargar datos desde el archivo CSV
df = pd.read_csv('pokemon.csv', encoding='utf-8')

# Barra lateral para filtros
with st.sidebar:
    st.subheader("Filtros")
    
    # Permitir al usuario seleccionar columnas para filtrar
    columnas_permitidas = ["Nombre", "Tipo 1", "Tipo 2", "Legendario"]
    selected_columns = st.multiselect("Seleccionar columnas para filtrar", columnas_permitidas)
    
    filters = {}
    
    for column in selected_columns:
        values = st.multiselect(f"Seleccionar valores de {column}", df[column].unique())
        if values:
            filters[column] = values

    
def aplicar_filtro(dataframe, filtros):
    filtered_data = dataframe.copy()
    
    for column, values in filtros.items():
        if values:
            # Construye una expresión de filtro dinámica
            filtro = " | ".join([f"`{column}` == '{value}'" for value in values])
            filtered_data = filtered_data.query(filtro)
    
    return filtered_data

# Aplicar filtros
filtered_data = aplicar_filtro(df, filters)

with st.container():
    # Resumen general de la aplicación
    st.title("Análisis de Datos de Pokémon")
    st.subheader("Este proyecto se enfoca en el análisis de datos de Pokémon, incluyendo la visualización y estudio de estadísticas diversas.")
    st.write("Habilidades utilizadas en este proyecto incluyen:")
    st.write("""
    1. Herramientas Básicas: Uso de Python, librerías y archivos CSV.
    2. Estadísticas Fundamentales: Media, Mediana y Desviación Estándar para comprender datos.
    3. Manipulación de Datos: Trabajo con datos desordenados y complejos.
    4. Visualización de Datos: Utilización de Matplotlib para representar gráficamente datos, facilitando su comprensión.
    """)

with st.container():
    st.write("---")
    # Sección de Datos Pokémon
    st.header("Datos Pokémon")
    st.caption("Tabla generada con Pandas desde datos del archivo CSV.")
    st.dataframe(filtered_data, width=1250)

with st.container():
    # Gráfico de Barras por Tipo 1
    st.write("---")
    st.header("Gráfico de Barras por Tipo 1")
    st.write("Este gráfico de barras horizontal muestra cuántos Pokémon pertenecen a cada tipo (Tipo 1) y permite una fácil comparación de la cantidad de Pokémon entre diferentes categorías.")
    st.caption("Gráfico de barras creado con Matplotlib utilizando datos de Pandas.")
    pokemon_count = df['Tipo 1'].value_counts()
    plt.figure(figsize=(12, 6))
    plt.bar(pokemon_count.index, pokemon_count.values,color='#00A2DA')
    plt.xlabel('Tipo 1')
    plt.ylabel('Cantidad')
    plt.title('Cantidad de Pokémon por Tipo 1')
    plt.xticks(rotation=45)
    plt.grid(True, axis='y', alpha=0.5, linestyle='--')
    st.pyplot(plt)

with st.container():
    # Gráfico heatmap
    st.write("---")
    st.header("Gráfico de Mapa de Calor")
    st.write("Este gráfico de calor te permite visualizar de manera efectiva cómo las diferentes estadísticas de los Pokémon están relacionadas entre sí.")
    st.caption("Gráfico de calor creado con Seaborn.")
    stats_selected = ['HP', 'Ataque', 'Defensa', 'Sp. Atk', 'Sp. Def', 'Velocidad']
    pokemon_stats = filtered_data[stats_selected]

    # Calcular la matriz de correlación
    correlation_matrix = pokemon_stats.corr()

    # Configurar el tamaño del heatmap
    plt.figure(figsize=(10, 8))

    # Crear el heatmap usando Seaborn
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")

    # Configurar título
    plt.title("Mapa de Calor de Correlación entre Estadísticas de Pokémon")

    # Mostrar el heatmap en Streamlit
    st.pyplot(plt)


with st.container():
    # Visualización de Datos Pokémon
    st.write("---")
    st.header("Visualización de Datos Pokémon")
    st.write("Este gráfico muestra la relación entre las estadísticas de Ataque y Defensa de los Pokémon, distinguiendo entre Pokémon legendarios y no legendarios.")
    st.caption("Gráfico de dispersión creado con Matplotlib.")
    st.write("")

    # Filtrar Pokémon Legendarios y no Legendarios en los datos filtrados
    legendary = filtered_data[filtered_data['Legendario'] == 'L']
    non_legendary = filtered_data[filtered_data['Legendario'] == 'N']

    # Gráfico de dispersión para Ataque vs. Defensa
    plt.figure(figsize=(10, 6))
    plt.scatter(legendary['Ataque'], legendary['Defensa'], label='Legendarios', color='#FFC50A', marker='*', s=50)
    plt.scatter(non_legendary['Ataque'], non_legendary['Defensa'], label='No Legendarios', color='#E11528', marker='o', s=30)

    # Etiquetas y título del gráfico
    plt.xlabel('Ataque')
    plt.ylabel('Defensa')
    plt.title('Relación entre Ataque y Defensa en Pokémon')

    # Leyenda
    plt.legend(['Legendarios', 'No Legendarios'])

    # Agregar líneas de cuadrícula verticales
    plt.grid(True, alpha=0.5, linestyle='--')

    # Mostrar el gráfico en Streamlit
    st.pyplot(plt)

with st.container():
    # Histograma de Velocidad de Pokémon
    st.write("---")
    st.header("Histograma de Velocidad de Pokémon")
    st.write("Este histograma muestra la distribución de las velocidades de los Pokémon después de aplicar filtros.")
    st.caption("Histograma creado con Matplotlib.")
    st.write("")

    # Crear un histograma de velocidad
    plt.figure(figsize=(10, 6))
    plt.hist(filtered_data['Velocidad'], bins=20, color='#C3121D', edgecolor='black')
    plt.xlabel('Velocidad')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de Velocidad de Pokémon')

    # Mostrar el histograma en Streamlit
    st.pyplot(plt)

with st.container():
    # Comparación de Pokémon
    st.write("---")
    st.header("Comparación de Pokémon")
    st.write("Selecciona dos Pokémon y luego muestra sus estadísticas en una tabla y un gráfico de barras para compararlas.")
    st.caption("Utilización de Tablas y Gráficos con Pandas y Matplotlib.")
    st.write("")

    # Crear un cuadro de selección para que el usuario elija dos Pokémon
    selected_pokemon = st.multiselect("Selecciona dos Pokémon para comparar", filtered_data['Nombre'])

    if len(selected_pokemon) == 2:
        # Filtrar los datos de los dos Pokémon seleccionados
        pokemon1 = filtered_data[filtered_data['Nombre'] == selected_pokemon[0]]
        pokemon2 = filtered_data[filtered_data['Nombre'] == selected_pokemon[1]]

        # Mostrar las estadísticas de los dos Pokémon seleccionados
        st.subheader(f"Comparando {selected_pokemon[0]} y {selected_pokemon[1]}")
        st.dataframe(pd.concat([pokemon1, pokemon2]), width=1250)

        # Crear un gráfico de barras para comparar las estadísticas
        stats = ['HP', 'Ataque', 'Defensa', 'Sp. Atk', 'Sp. Def', 'Velocidad']
        values_pokemon1 = [pokemon1[stat].values[0] for stat in stats]
        values_pokemon2 = [pokemon2[stat].values[0] for stat in stats]

        plt.figure(figsize=(10, 6))
        x = range(len(stats))
        width = 0.4
        plt.bar(x, values_pokemon1, width=width, label=selected_pokemon[0])
        plt.bar([i + width for i in x], values_pokemon2, width=width, label=selected_pokemon[1])
        plt.xlabel('Estadísticas')
        plt.ylabel('Valor')
        plt.title('Comparación de Estadísticas de Pokémon')
        plt.xticks([i + width/2 for i in x], stats)
        plt.legend()
        st.pyplot(plt)
    else:
        st.warning("Selecciona exactamente 2 Pokémon para comparar")

