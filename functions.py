# Importación de las librerías necesarias 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_random_data(size=10):
    """Genera un array de datos aleatorios."""
    return np.random.rand(size)

def create_dataframe(data):
    """Crea un DataFrame de pandas a partir de los datos proporcionados."""
    return pd.DataFrame(data, columns=['Valores'])

def load_dataset(filepath):
    """Carga el dataset desde un archivo CSV."""
    try:
        dataset = pd.read_csv(filepath)
        print(f"Dataset cargado exitosamente desde {filepath}.")
        return dataset
    except FileNotFoundError:
        print(f"Error: El archivo no se encuentra en la ruta {filepath}.")
        return None

def visualize_data(df):
    """Visualiza los datos en un gráfico de línea."""
    plt.figure(figsize=(8, 4))
    sns.lineplot(data=df, x=df.index, y='Valores')
    plt.title('Gráfico de Línea de Valores Aleatorios')
    plt.xlabel('Índice')
    plt.ylabel('Valores')
    plt.grid()
    plt.show()
