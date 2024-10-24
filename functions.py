# Importación de librerías 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def read_raw_energy_data():
    """Lee el dataset original."""
    energy_csv_url = 'https://nyc3.digitaloceanspaces.com/owid-public/data/energy/owid-energy-data.csv'
    #energy_csv_url = './data/owid-energy-data.csv'
    return pd.read_csv(energy_csv_url)


def read_raw_energy_codebook():
    """Lee la descripción del dataset original."""
    codebook_csv_url = 'https://github.com/owid/energy-data/raw/master/owid-energy-codebook.csv'
    #codebook_csv_url = './data/owid-energy-codebook.csv'
    return pd.read_csv(codebook_csv_url)


def read_raw_country_info():
    """Lee el dataset de información de los paises."""
    country_info_json_url = 'https://gist.github.com/Yizack/bbfce31e0217a3689c8d961a356cb10d/raw/7ffa5b94615c6681d68c54fe7edcca098fae180b/countries.json'
    #country_info_json_url = './data/countries.json'
    json_data = pd.read_json(country_info_json_url)
    countries_data = json_data['countries']
    return pd.DataFrame(countries_data.tolist())


def read_config():
    """Lee el archivo de configuración."""
    config = './columns.xlsx'
    return pd.read_excel(config)


def drop_aggregated_data(dataset, columns_to_check):
    """Elimina las columnas que contienen información aggregada."""
    return dataset.dropna(subset=columns_to_check)


def keep_and_rename_columns(dataset, config):
    """Filtra y renombra las columnas del dataset."""
    columns_to_keep = config['id']
    rename_mapping = config.set_index('id')['Columna'].to_dict()
    return dataset[columns_to_keep].rename(columns=rename_mapping)


def datatype_conversion(dataset):
    """Convierte los tipos de datos de las columnas."""
    # Convertir 'Año' a tipo entero, si es necesario
    dataset['Año'] = dataset['Año'].astype(int)

    # Rondear columnas de tipo float a enteros
    float_columns = dataset.select_dtypes(include=['float64']).columns
    rounded_floats = dataset[float_columns].round(0).fillna(0).astype(int)
    dataset[float_columns] = rounded_floats
    return dataset


def interpolate_missing_data(dataset, groupby_column, column_to_fill):
    """Interpolación de datos faltantes."""
    dataset[column_to_fill] = dataset.groupby(groupby_column)[column_to_fill].transform(lambda x: x.interpolate())
    return dataset


def dataset_info(dataset):
    """Muestra información básica del dataset."""
    print("\nPrimeras filas del dataset:")
    print(dataset.head())
    
    print("\nÚltimas filas del dataset:")
    print(dataset.tail())
    
    print("\nInformación del dataset:")
    print(dataset.info())
    
    print("\nEstadísticas descriptivas:")
    print(dataset.describe(include='all'))
    
    print("\nColumnas del dataset:")
    print(dataset.columns)

    print("\nVisualización de la distribución de algunas columnas numéricas")
    numerical_columns = dataset.select_dtypes(include=['float64', 'int64']).columns[:16]  # Limita a 16 columnas

    plt.figure(figsize=(15, 10))
    for i, column in enumerate(numerical_columns):
        plt.subplot(4, 4, i + 1)
        sns.histplot(dataset[column], bins=30, kde=True)
        plt.title(column)
    plt.tight_layout()
    plt.show()
    

def filter_dataframe(dataset, column_name, value):
    """Filtra el DataFrame por un valor específico en una columna."""
    if column_name in dataset.columns:
        filtered_df = dataset[dataset[column_name] == value]
        print(f"\nSe han encontrado {filtered_df.shape[0]} filas donde {column_name} es igual a {value}.")
        return filtered_df
    else:
        print(f"Error: La columna '{column_name}' no existe en el DataFrame.")
        return dataset  # Retorna el DataFrame sin filtrar si la columna no existe.


def plot_data(dataset):
    """Genera un gráfico de barras a partir del DataFrame."""
    plt.figure(figsize=(10, 6))
    sns.barplot(data=dataset, x='Año', y='Electricidad de Energías Renovables', palette='viridis')
    plt.title('Electricidad de Energías Renovables por año')
    plt.xlabel('Año')
    plt.ylabel('Electricidad de Energías Renovables')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
