# Importación de librerías

from sqlalchemy import create_engine
from os import getenv
from dotenv import load_dotenv
from pandas import read_sql_query


# Cargar variables de entorno
load_dotenv()


# Conectar a la base de datos
def connect_to_db(schema):
    user = getenv('MYSQL_USER')
    password = getenv('MYSQL_PASSWORD')
    host = 'localhost'
    
    # Crear el motor de conexión
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{schema}')
    return engine


def df_to_mysql_table(df, table_name, engine):
    connection = engine.connect()
    df.to_sql(table_name, con=connection, if_exists='replace', index=False)
    print(f"La tabla '{table_name}' se ha insertado exitosamente en la base de datos.")
    connection.close()


def select_data_for_powerbi(engine, query):
    """Función para seleccionar los datos de la base de datos."""
    try:
        return read_sql_query(query, engine)
    except:
        return None