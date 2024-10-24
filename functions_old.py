# Importación de librerías 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_raw_energy_data():
    """Lee el dataset original."""
    energy_csv_url = 'https://nyc3.digitaloceanspaces.com/owid-public/data/energy/owid-energy-data.csv'
    return pd.read_csv(energy_csv_url)

def read_raw_energy_codebook():
    """Lee el dataset original."""
    codebook_csv_url = 'https://github.com/owid/energy-data/blob/master/owid-energy-codebook.csv'
    return pd.read_csv(codebook_csv_url)

def read_raw_country_info():
    """Lee el dataset de información de los paises."""
    country_info_json_url = 'https://gist.github.com/Yizack/bbfce31e0217a3689c8d961a356cb10d/raw/7ffa5b94615c6681d68c54fe7edcca098fae180b/countries.json'
    return pd.read_json(country_info_json_url)


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

def dataset_info(dataset):
    """Muestra información básica del dataset."""
    print("\nPrimeras filas del dataset:")
    print(dataset.head())
    
    print("\nÚltimas filas del dataset:")
    print(dataset.tail())
    
    print("\nInformación del dataset:")
    print(dataset.info())
    
    #print("\nValores nulos por columna:")
    #print(dataset.isnull().sum())
    
    print("\nEstadísticas descriptivas:")
    print(dataset.describe())
    
    print("\nColumnas del dataset:")
    print(dataset.columns)
    
# Diccionario de traducciones
translations = {
    'Afghanistan': 'Afganistán',
    'Albania': 'Albania',
    'Algeria': 'Argelia',
    'Andorra': 'Andorra',
    'Angola': 'Angola',
    'Antigua and Barbuda': 'Antigua y Barbuda',
    'Argentina': 'Argentina',
    'Armenia': 'Armenia',
    'Australia': 'Australia',
    'Austria': 'Austria',
    'Azerbaijan': 'Azerbaiyán',
    'Bahamas': 'Las Bahamas',
    'Bahrain': 'Baréin',
    'Bangladesh': 'Bangladés',
    'Barbados': 'Barbados',
    'Belarus': 'Bielorrusia',
    'Belgium': 'Bélgica',
    'Belize': 'Belice',
    'Benin': 'Benín',
    'Bhutan': 'Bután',
    'Bolivia': 'Bolivia',
    'Bosnia and Herzegovina': 'Bosnia y Herzegovina',
    'Botswana': 'Botsuana',
    'Brazil': 'Brasil',
    'Brunei': 'Brunéi',
    'Bulgaria': 'Bulgaria',
    'Burkina Faso': 'Burkina Faso',
    'Burundi': 'Burundi',
    'Cabo Verde': 'Cabo Verde',
    'Cambodia': 'Camboya',
    'Cameroon': 'Camerún',
    'Canada': 'Canadá',
    'Central African Republic': 'República Centroafricana',
    'Chad': 'Chad',
    'Chile': 'Chile',
    'China': 'China',
    'Colombia': 'Colombia',
    'Comoros': 'Comoras',
    'Congo': 'Congo',
    'Costa Rica': 'Costa Rica',
    'Croatia': 'Croacia',
    'Cuba': 'Cuba',
    'Cyprus': 'Chipre',
    'Czechia': 'República Checa',
    'Democratic Republic of the Congo': 'República Democrática del Congo',
    'Denmark': 'Dinamarca',
    'Dominica': 'Dominica',
    'Dominican Republic': 'República Dominicana',
    'Ecuador': 'Ecuador',
    'Egypt': 'Egipto',
    'El Salvador': 'El Salvador',
    'Equatorial Guinea': 'Guinea Ecuatorial',
    'Eritrea': 'Eritrea',
    'Estonia': 'Estonia',
    'Eswatini': 'Suazilandia',
    'Ethiopia': 'Etiopía',
    'Fiji': 'Fiyi',
    'Finland': 'Finlandia',
    'France': 'Francia',
    'Gabon': 'Gabón',
    'Georgia': 'Georgia',
    'Germany': 'Alemania',
    'Ghana': 'Ghana',
    'Greece': 'Grecia',
    'Grenada': 'Granada',
    'Guatemala': 'Guatemala',
    'Guinea': 'Guinea',
    'Guinea-Bissau': 'Guinea-Bisáu',
    'Guyana': 'Guyana',
    'Haiti': 'Haití',
    'Honduras': 'Honduras',
    'Hungary': 'Hungría',
    'Iceland': 'Islandia',
    'India': 'India',
    'Indonesia': 'Indonesia',
    'Iran': 'Irán',
    'Iraq': 'Irak',
    'Ireland': 'Irlanda',
    'Israel': 'Israel',
    'Italy': 'Italia',
    'Jamaica': 'Jamaica',
    'Japan': 'Japón',
    'Jordan': 'Jordania',
    'Kazakhstan': 'Kazajistán',
    'Kenya': 'Kenia',
    'Kiribati': 'Kiribati',
    'Kuwait': 'Kuwait',
    'Kyrgyzstan': 'Kirguistán',
    'Laos': 'Laos',
    'Latvia': 'Letonia',
    'Lebanon': 'Líbano',
    'Lesotho': 'Lesoto',
    'Liberia': 'Liberia',
    'Libya': 'Libia',
    'Liechtenstein': 'Liechtenstein',
    'Lithuania': 'Lituania',
    'Luxembourg': 'Luxemburgo',
    'Madagascar': 'Madagascar',
    'Malawi': 'Malawi',
    'Malaysia': 'Malasia',
    'Maldives': 'Maldivas',
    'Mali': 'Mali',
    'Malta': 'Malta',
    'Marshall Islands': 'Islas Marshall',
    'Mauritania': 'Mauritania',
    'Mauritius': 'Mauricio',
    'Mexico': 'México',
    'Micronesia': 'Micronesia',
    'Moldova': 'Moldavia',
    'Monaco': 'Mónaco',
    'Mongolia': 'Mongolia',
    'Montenegro': 'Montenegro',
    'Morocco': 'Marruecos',
    'Mozambique': 'Mozambique',
    'Myanmar': 'Myanmar',
    'Namibia': 'Namibia',
    'Nauru': 'Nauru',
    'Nepal': 'Nepal',
    'Netherlands': 'Países Bajos',
    'New Zealand': 'Nueva Zelanda',
    'Nicaragua': 'Nicaragua',
    'Niger': 'Níger',
    'Nigeria': 'Nigeria',
    'North America': 'América del Norte',
    'North Korea': 'Corea del Norte',
    'North Macedonia': 'Macedonia del Norte',
    'Norway': 'Noruega',
    'Oceania': 'Oceanía',
    'Pakistan': 'Pakistán',
    'Palau': 'Palaos',
    'Palestine': 'Palestina',
    'Panama': 'Panamá',
    'Papua New Guinea': 'Papúa Nueva Guinea',
    'Paraguay': 'Paraguay',
    'Peru': 'Perú',
    'Philippines': 'Filipinas',
    'Poland': 'Polonia',
    'Portugal': 'Portugal',
    'Qatar': 'Catar',
    'Romania': 'Rumania',
    'Russia': 'Rusia',
    'Rwanda': 'Ruanda',
    'Saint Barthélemy': 'San Bartolomé',
    'Saint Helena': 'Santa Elena',
    'Saint Kitts and Nevis': 'San Cristóbal y Nieves',
    'Saint Lucia': 'Santa Lucía',
    'Saint Martin': 'San Martín',
    'Saint Pierre and Miquelon': 'San Pedro y Miquelón',
    'Saint Vincent and the Grenadines': 'San Vicente y las Granadinas',
    'Samoa': 'Samoa',
    'San Marino': 'San Marino',
    'Sao Tome and Principe': 'Santo Tomé y Príncipe',
    'Saudi Arabia': 'Arabia Saudita',
    'Senegal': 'Senegal',
    'Serbia': 'Serbia',
    'Seychelles': 'Seychelles',
    'Sierra Leone': 'Sierra Leona',
    'Singapore': 'Singapur',
    'Slovakia': 'Eslovaquia',
    'Slovenia': 'Eslovenia',
    'Solomon Islands': 'Islas Salomón',
    'Somalia': 'Somalia',
    'South Africa': 'Sudáfrica',
    'South America (EI)': 'América del Sur (EI)',
    'South Korea': 'Corea del Sur',
    'South Sudan': 'Sudán del Sur',
    'Spain': 'España',
    'Sri Lanka': 'Sri Lanka',
    'Sudan': 'Sudán',
    'Suriname': 'Surinam',
    'Sweden': 'Suecia',
    'Switzerland': 'Suiza',
    'Taiwan': 'Taiwán',
    'Tajikistan': 'Tayikistán',
    'Tanzania': 'Tanzania',
    'Thailand': 'Tailandia',
    'Timor-Leste': 'Timor-Leste',
    'Togo': 'Togo',
    'Tonga': 'Tonga',
    'Trinidad and Tobago': 'Trinidad y Tobago',
    'Tunisia': 'Túnez',
    'Turkey': 'Turquía',
    'Turkmenistan': 'Turkmenistán',
    'Tuvalu': 'Tuvalu',
    'Uganda': 'Uganda',
    'Ukraine': 'Ucrania',
    'United Arab Emirates': 'Emiratos Árabes Unidos',
    'United Kingdom': 'Reino Unido',
    'United States': 'Estados Unidos',
    'Uruguay': 'Uruguay',
    'Uzbekistan': 'Uzbekistán',
    'Vanuatu': 'Vanuatu',
    'Vatican City': 'Ciudad del Vaticano',
    'Venezuela': 'Venezuela',
    'Vietnam': 'Vietnam',
    'Yemen': 'Yemen',
    'Zambia': 'Zambia',
    'Zimbabwe': 'Zimbabue'
}

# Cargar el archivo CSV
file_path = 'data/owid-energy-data.csv'
data = load_dataset(file_path)

if data is not None:
    # Verificar nombres de columnas
    print(data.columns)
    
    # Reemplazar los nombres de los países
    if 'country' in data.columns:
        data['country'] = data['country'].replace(translations)
    else:
        print("La columna 'country' no se encuentra en el dataset.")

    # Verificar los valores únicos después del reemplazo
    print(data['country'].unique())

    # Mostrar información básica del dataset
    dataset_info(data)

def rename_columns(dataset):  # Cambia 'df' a 'dataset'
    """Renombra las columnas del dataset al español."""
    column_names = {
        'country': 'País',
        'year': 'Año',
        'iso_code': 'Código ISO',
        'population': 'Población',
        'gdp': 'PIB',
        'biofuel_cons_change_pct': 'Cambio porcentual en el consumo de biocombustibles',
        'biofuel_cons_change_twh': 'Consumo de biocombustibles medido en teravatios-hora (TWh)',
        'biofuel_cons_per_capita': 'Consumo de biocombustibles por persona',
        'biofuel_consumption': 'Consumo total de biocombustibles',
        'biofuel_elec_per_capita': 'Electricidad generada a partir de biocombustibles por persona',
        'biofuel_electricity': 'Electricidad generada a partir de biocombustibles',
        'biofuel_share_elec': 'Proporción de la energía de biocombustibles en la producción total de electricidad',
        'biofuel_share_energy': 'Participación de la energía de biocombustibles en el consumo total de energía',
        'carbon_intensity_elec': 'Intensidad de carbono de la electricidad',
        'coal_cons_change_pct': 'Cambio porcentual en el consumo de carbón',
        'coal_cons_change_twh': 'Cambio en el consumo de carbón medido en teravatios-hora (TWh)',
        'coal_cons_per_capita': 'Consumo de carbón por persona',
        'coal_consumption': 'Consumo total de carbón',
        'coal_elec_per_capita': 'Electricidad generada a partir de carbón por persona',
        'coal_electricity': 'Electricidad generada a partir de carbón',
        'coal_prod_change_pct': 'Cambio porcentual en la producción de carbón',
        'coal_prod_change_twh': 'Cambio en la producción de carbón medido en teravatios-hora (TWh)',
        'coal_prod_per_capita': 'Producción de carbón por persona',
        'coal_production': 'Producción total de carbón',
        'coal_share_elec': 'Proporción de carbón en la producción total de electricidad',
        'coal_share_energy': 'Participación del carbón en el consumo total de energía',
        'electricity_demand': 'Demanda de electricidad',
        'electricity_demand_per_capita': 'Demanda de electricidad por persona',
        'electricity_generation': 'Generación de electricidad',
        'electricity_share_energy': 'Participación de la electricidad en el consumo total de energía',
        'energy_cons_change_pct': 'Cambio porcentual en el consumo de energía',
        'energy_cons_change_twh': 'Cambio en el consumo de energía medido en teravatios-hora (TWh)',
        'energy_per_capita': 'Energía consumida por persona',
        'energy_per_gdp': 'Energía consumida por PIB',
        'fossil_cons_change_pct': 'Cambio porcentual en el consumo de fósiles',
        'fossil_cons_change_twh': 'Cambio en el consumo de fósiles medido en teravatios-hora (TWh)',
        'fossil_elec_per_capita': 'Electricidad generada a partir de fósiles por persona',
        'fossil_electricity': 'Electricidad generada a partir de fósiles',
        'fossil_energy_per_capita': 'Cantidad de energía fósil disponible o generada por persona',
        'fossil_fuel_consumption': 'Consumo total de combustibles fósiles',
        'fossil_share_elec': 'Proporción de fósiles en la producción total de electricidad',
        'fossil_share_energy': 'Participación de fósiles en el consumo total de energía',
        'gas_cons_change_pct': 'Cambio porcentual en el consumo de gas',
        'gas_cons_change_twh': 'Cambio en el consumo de gas medido en teravatios-hora (TWh)',
        'gas_consumption': 'Consumo total de gas',
        'gas_elec_per_capita': 'Electricidad generada a partir de gas por persona',
        'gas_electricity': 'Electricidad generada a partir de gas',
        'gas_energy_per_capita': 'Cantidad de energía de gas disponible o generada por persona',
        'gas_prod_change_pct': 'Cambio porcentual en la producción de gas',
        'gas_prod_change_twh': 'Cambio en la producción de gas medido en teravatios-hora (TWh)',
        'gas_prod_per_capita': 'Producción de gas por persona',
        'gas_production': 'Producción total de gas',
        'gas_share_elec': 'Proporción de gas en la producción total de electricidad',
        'gas_share_energy': 'Participación del gas en el consumo total de energía',
        'greenhouse_gas_emissions': 'Emisiones de gases de efecto invernadero',
        'hydro_cons_change_pct': 'Cambio porcentual en el consumo de hidroeléctrico',
        'hydro_cons_change_twh': 'Cambio en el consumo de hidroeléctrico medido en teravatios-hora (TWh)',
        'hydro_consumption': 'Consumo total de energía hidroeléctrica',
        'hydro_elec_per_capita': 'Electricidad generada a partir de hidroeléctrico por persona',
        'hydro_electricity': 'Electricidad generada a partir de energía hidroeléctrica',
        'hydro_energy_per_capita': 'Cantidad de energía hidroeléctrica disponible o generada por persona',
        'hydro_share_elec': 'Proporción de la energía hidroeléctrica en la producción total de electricidad',
        'hydro_share_energy': 'Participación de la energía hidroeléctrica en el consumo total de energía',
        'low_carbon_cons_change_pct': 'Cambio porcentual en el consumo de energías de bajo carbono',
        'low_carbon_cons_change_twh': 'Cambio en el consumo de energías de bajo carbono medido en teravatios-hora (TWh)',
        'low_carbon_consumption': 'Consumo total de energías de bajo carbono',
        'low_carbon_elec_per_capita': 'Electricidad generada a partir de energías de bajo carbono por persona',
        'low_carbon_electricity': 'Electricidad generada a partir de energías de bajo carbono',
        'low_carbon_energy_per_capita': 'Cantidad de energía de bajo carbono disponible o generada por persona',
        'low_carbon_share_elec': 'Proporción de energías de bajo carbono en la producción total de electricidad',
        'low_carbon_share_energy': 'Participación de energías de bajo carbono en el consumo total de energía',
        'net_elec_imports': 'Importaciones netas de electricidad',
        'net_elec_imports_share_demand': 'Participación de las importaciones netas de electricidad en la demanda',
        'nuclear_cons_change_pct': 'Cambio porcentual en el consumo de energía nuclear',
        'nuclear_cons_change_twh': 'Cambio en el consumo de energía nuclear medido en teravatios-hora (TWh)',
        'nuclear_consumption': 'Consumo total de energía nuclear',
        'nuclear_elec_per_capita': 'Electricidad generada a partir de energía nuclear por persona',
        'nuclear_electricity': 'Electricidad generada a partir de energía nuclear',
        'nuclear_energy_per_capita': 'Cantidad de energía nuclear disponible o generada por persona',
        'nuclear_share_elec': 'Proporción de energía nuclear en la producción total de electricidad',
        'nuclear_share_energy': 'Participación de energía nuclear en el consumo total de energía',
        'oil_cons_change_pct': 'Cambio porcentual en el consumo de petróleo',
        'oil_cons_change_twh': 'Cambio en el consumo de petróleo medido en teravatios-hora (TWh)',
        'oil_consumption': 'Consumo total de petróleo',
        'oil_elec_per_capita': 'Electricidad generada a partir de petróleo por persona',
        'oil_electricity': 'Electricidad generada a partir de petróleo',
        'oil_energy_per_capita': 'Cantidad de energía de petróleo disponible o generada por persona',
        'oil_prod_change_pct': 'Cambio porcentual en la producción de petróleo',
        'oil_prod_change_twh': 'Cambio en la producción de petróleo medido en teravatios-hora (TWh)',
        'oil_prod_per_capita': 'Producción de petróleo por persona',
        'oil_production': 'Producción total de petróleo',
        'oil_share_elec': 'Proporción de petróleo en la producción total de electricidad',
        'oil_share_energy': 'Participación del petróleo en el consumo total de energía',
        'other_renewable_consumption': 'Consumo total de otras energías renovables',
        'other_renewable_electricity': 'Electricidad generada a partir de otras energías renovables',
        'other_renewable_exc_biofuel_electricity': 'Electricidad generada a partir de otras renovables excluyendo biocombustibles',
        'other_renewables_cons_change_pct': 'Cambio porcentual en el consumo de otras energías renovables',
        'other_renewables_cons_change_twh': 'Cambio en el consumo de otras energías renovables medido en teravatios-hora (TWh)',
        'other_renewables_elec_per_capita': 'Electricidad generada a partir de otras energías renovables por persona',
        'other_renewables_energy_per_capita': 'Cantidad de energía de otras renovables disponible o generada por persona',
        'other_renewables_share_elec': 'Proporción de otras energías renovables en la producción total de electricidad',
        'other_renewables_share_elec_exc_biofuel': 'Proporción de otras renovables excluyendo biocombustibles en la producción total de electricidad',
        'other_renewables_share_energy': 'Participación de otras energías renovables en el consumo total de energía',
        'primary_energy_consumption': 'Consumo total de energía primaria',
        'renewables_cons_change_pct': 'Cambio porcentual en el consumo de energías renovables',
        'renewables_cons_change_twh': 'Cambio en el consumo de energías renovables medido en teravatios-hora (TWh)',
        'renewables_consumption': 'Consumo total de energías renovables',
        'renewables_elec_per_capita': 'Electricidad generada a partir de energías renovables por persona',
        'renewables_electricity': 'Electricidad generada a partir de energías renovables',
        'renewables_energy_per_capita': 'Cantidad de energía renovable disponible o generada por persona',
        'renewables_share_elec': 'Proporción de energías renovables en la producción total de electricidad',
        'renewables_share_energy': 'Participación de energías renovables en el consumo total de energía',
        'solar_cons_change_pct': 'Cambio porcentual en el consumo de energía solar',
        'solar_cons_change_twh': 'Cambio en el consumo de energía solar medido en teravatios-hora (TWh)',
        'solar_consumption': 'Consumo total de energía solar',
        'solar_elec_per_capita': 'Electricidad generada a partir de energía solar por persona',
        'solar_electricity': 'Electricidad generada a partir de energía solar',
        'solar_energy_per_capita': 'Cantidad de energía solar disponible o generada por persona',
        'solar_share_elec': 'Proporción de energía solar en la producción total de electricidad',
        'solar_share_energy': 'Participación de la energía solar en el consumo total de energía',
        'wind_cons_change_pct': 'Cambio porcentual en el consumo de energía eólica',
        'wind_cons_change_twh': 'Cambio en el consumo de energía eólica medido en teravatios-hora (TWh)',
        'wind_consumption': 'Consumo total de energía eólica',
        'wind_elec_per_capita': 'Electricidad generada a partir de energía eólica por persona',
        'wind_electricity': 'Electricidad generada a partir de energía eólica',
        'wind_energy_per_capita': 'Cantidad de energía eólica disponible o generada por persona',
        'wind_share_elec': 'Proporción de energía eólica en la producción total de electricidad',
        'wind_share_energy': 'Participación de energía eólica en el consumo total de energía',
        'yearly_renewable_energy': 'Año de la energía renovable',
        'yearly_biofuel': 'Año del biocombustible',
        'yearly_coal': 'Año del carbón',
        'yearly_fossil': 'Año de fósiles',
        'yearly_gas': 'Año del gas',
        'yearly_hydro': 'Año de hidroeléctrico',
        'yearly_nuclear': 'Año de energía nuclear',
        'yearly_oil': 'Año del petróleo',
        'yearly_solar': 'Año de energía solar',
        'yearly_wind': 'Año de energía eólica',
        'total_consumption': 'Consumo total'
    }

    dataset.rename(columns=column_names, inplace=True)
    print("Columnas renombradas exitosamente.")
    return dataset  # Asegúrate de retornar el DataFrame

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
    sns.barplot(data=dataset, x='Año', y='Consumo total de biocombustibles', palette='viridis')
    plt.title('Consumo total de biocombustibles por año')
    plt.xlabel('Año')
    plt.ylabel('Consumo total de biocombustibles')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    # Ejemplo de uso
    data = generate_random_data()
    df = create_dataframe(data)
    print(df)
    
    # Cargar un dataset desde un archivo
    dataset = load_dataset('data/owid-energy-data.csv')
    
    if dataset is not None:
        dataset_info(dataset)
        rename_columns(dataset)
        
        # Filtrar el DataFrame por un valor específico
        filtered_df = filter_dataframe(dataset, 'Año', 2020)
        print(filtered_df)
        
        # Graficar los datos
        plot_data(filtered_df)

if __name__ == "__main__":
    main()