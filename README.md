# Análisis de Datos de Pokémon con Streamlit

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)]([https://www.streamlit.com/](https://lucianoproyectopokemon.streamlit.app/))

![image](https://github.com/LUXI4NO/AnalystData-Pokemon/assets/140111840/61610e38-7529-4d34-8bf6-83dae959c361)

---

## Descripción

Este proyecto es una aplicación de análisis de datos de Pokémon creada con Streamlit. Proporciona una interfaz interactiva que te permite explorar y visualizar datos relacionados con los Pokémon. Puedes filtrar los datos, ver tablas, gráficos y comparar estadísticas de diferentes Pokémon.

---

## Tabla de Contenido

- [CSV para realizar el Proyecto](#csv-para-realizar-el-proyecto)
- [Requisitos](#requisitos)
- [Instrucciones de Uso](#instrucciones-de-uso)
- [Características](#características)
- [Capturas de Pantalla](#capturas-de-pantalla)
- [Realización del Gráfico](#realización-del-gráfico)
- [Datos](#datos)
- [Enlaces](#enlaces)

---
## Librerias Python Utilizadas
```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

## CSV para realizar el Proyecto
El archivo pokemon.csv contiene información valiosa sobre los primeros 151 Pokémon, incluyendo sus tipos, estadísticas y otros atributos que son fundamentales para entender sus habilidades y características en el mundo de Pokémon.
```python
# Cargar datos desde el archivo CSV
df = pd.read_csv('pokemon.csv', encoding='utf-8')
```

## Requisitos
Asegúrate de tener las siguientes bibliotecas instaladas en tu entorno de desarrollo. Puedes instalarlas utilizando el archivo requirements.txt incluido en este proyecto.

```bash
pip install -r requirements.txt
```


## Instrucciones de Uso
Una vez que hayas configurado el entorno y las dependencias, puedes ejecutar la aplicación de Streamlit con el siguiente comando:
```bash
streamlit run Proyecto.py
```

## Características
- Filtra y explora datos de Pokémon.
- Visualiza tablas de datos.
- Crea gráficos de barras, mapas de calor y gráficos de dispersión.
- Compara estadísticas de dos Pokémon seleccionados.
- Interfaz interactiva y fácil de usar.

## Capturas de Pantalla

![image](https://github.com/LUXI4NO/AnalystData-Pokemon/assets/140111840/ae149618-f1c6-4119-b0a8-c8729617b824)


## Realización del Gráfico

``` Python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(legendary['Ataque'], legendary['Defensa'],  label='Legendarios', color='#FFC50A', marker='*', s=50)
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

```

## Datos
Los datos utilizados en este proyecto se encuentran en el archivo pokemon.csv. Este archivo contiene información sobre los Pokémon, incluyendo sus nombres, tipos, estadísticas, generación y si son legendarios o no.

## Enlaces
- [![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)]([https://github.com/](https://github.com/LUXI4NO))
- [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:alvarezlucianoezequiel@gmail.com)
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luciano-alvarez-332843285/)
