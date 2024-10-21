
from functions import generate_random_data, create_dataframe, load_dataset, visualize_data

def main():
    """Función principal del programa."""
    # Cargar el dataset
    filepath = r"D:\Documents\GitHub\world-energy-consumption\data\owid-energy-data.csv"
    dataset = load_dataset(filepath)
    
    if dataset is not None:
        # Aquí puedes realizar otras operaciones con el dataset
        print(dataset.head())  # Muestra las primeras filas del dataset

        # Generar datos aleatorios (puedes eliminar esto si no lo necesitas)
        random_data = generate_random_data(size=10)

        # Crear un DataFrame de ejemplo
        df = create_dataframe(random_data)

        # Visualizar los datos
        visualize_data(df)

if __name__ == "__main__":
    main()