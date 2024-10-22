import os
import pandas as pd
from functions import generate_random_data, create_dataframe, load_dataset, visualize_data, rename_columns

def main():
    """Función principal del programa."""
    # Cargar el dataset
    filepath = r"D:\Documents\GitHub\world-energy-consumption\data\owid-energy-data.csv"
    dataset = load_dataset(filepath)

    if dataset is not None:
        print("Dataset cargado exitosamente:")
        print(dataset.head())  # Muestra las primeras filas del dataset

        # Mostrar columnas originales
        print("Columnas originales del dataset:")
        print(dataset.columns)

        # Renombrar las columnas al español
        dataset = rename_columns(dataset)

        if dataset is not None:  # Verifica que el DataFrame no sea None
            print("Primeras filas del dataset después de renombrar columnas:")
            print(dataset.head())  # Muestra las primeras filas del dataset
            print("Columnas después del renombrado:")
            print(dataset.columns)

            # Crear un DataFrame de ejemplo (elimina esto si no lo necesitas)
            random_data = generate_random_data(size=10)
            df = create_dataframe(random_data)

            # Visualizar los datos
            visualize_data(df)

            # Guardar el DataFrame limpio en un archivo CSV
            output_folder = r"D:\Documents\GitHub\world-energy-consumption\cleaned"  # Ruta de la carpeta
            output_file = os.path.join(output_folder, "energy_data_cleaned.csv")  # Nombre del archivo

            # Crear la carpeta si no existe
            os.makedirs(output_folder, exist_ok=True)

            # Guardar el DataFrame como CSV
            dataset.to_csv(output_file, index=False, encoding='utf-8')
            print(f"El dataset limpio se ha guardado en: {output_file}")
        else:
            print("Error: El DataFrame después de renombrar columnas es None.")

if __name__ == "__main__":
    main()

