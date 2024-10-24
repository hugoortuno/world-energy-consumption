from functions import read_raw_energy_data, read_raw_energy_codebook, read_raw_country_info, read_config, drop_aggregated_data, keep_and_rename_columns, interpolate_missing_data, datatype_conversion, dataset_info, filter_dataframe, plot_data
from database import connect_to_db, df_to_mysql_table, select_data_for_powerbi


def main():
    """Función principal del programa."""
    # Conectar a la base de datos
    energy_engine = connect_to_db('energy')
    print("Conectado a la base de datos.")

    # Cargar los datos y guardar una copia de los datos en bruto en la base de datos
    energy_df = read_raw_energy_data()
    df_to_mysql_table(energy_df, 'energy_data_raw', energy_engine)
    codebook_df = read_raw_energy_codebook()
    df_to_mysql_table(codebook_df, 'codebook_raw', energy_engine)
    country_info_df = read_raw_country_info()
    df_to_mysql_table(country_info_df, 'country_info_raw', energy_engine)

    # Quitar datos agregados
    energy_df_cleaned = drop_aggregated_data(energy_df, ['iso_code', 'country', 'year'])

    # Reemplazar nombres de columnas y quitar las no necesarias
    config_df = read_config()
    energy_df_cleaned = keep_and_rename_columns(energy_df_cleaned, config_df)

    # Interpolación de datos faltantes
    energy_df_cleaned.sort_values(by=['País', 'Año'], inplace=True)
    energy_df_cleaned = interpolate_missing_data(energy_df_cleaned, 'País', 'PIB (Producto Interno Bruto)')

    # Cambio de tipo de datos
    energy_df_cleaned = datatype_conversion(energy_df_cleaned)
    print('Datos limpidas y procesadas con éxito.')

    # Guardar los datos procesados en la base de datos
    df_to_mysql_table(energy_df_cleaned, 'energy_data', energy_engine)

    # Información del dataset
    dataset_info(energy_df_cleaned)

    # Vizualización de los datos con Python
    plot_data(energy_df_cleaned)

    # selección de datos para PowerBI de la base de datos
    # consulta SQL
    query = """
    SELECT *
    FROM `energy`.`energy_data` AS e
    JOIN (
        SELECT Region AS `Región`, LifeExpectancy AS `Expectativa de vida`, Code
        FROM world.country
    ) AS w ON e.`Código ISO` = w.`Code`
    JOIN (
        SELECT name_es AS `País ES`, continent_es AS Continente, km2 AS `Superficie, km2`, code_3 
        FROM energy.country_info_raw
    ) AS c ON e.`Código ISO` = c.code_3;
    """
    # executar la consulta
    df = select_data_for_powerbi(energy_engine, query)

    if df.empty:
        print("La consulta no resultó exitosa")
    else:
        print('Datos seleccionadas para PowerBI con éxito.')
        
    # exportar los datos a un archivo Excel
    excel_filename = './cleaned/energy_data.xlsx'
    df.to_excel(excel_filename, index=False)
    print(f"Data saved to {excel_filename}")

    # Cerrar la base de datos
    energy_engine.dispose()

    print("¡Bien hecho, lo conseguimos!")


if __name__ == "__main__":
    main()

