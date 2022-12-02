from etldagster.create_db import create_database, drop_table, create_table
from dagster import op
import pandas as pd

@op
def load_table():

    #create database and table
    conn = create_database()

    drop_table(conn)
    create_table(conn)
    
    df = pd.read_excel('etldagster/data/Matriz_adyacencia.xlsx', engine='openpyxl', skiprows=1, index_col=0)

    df = (df
    .set_index(['Unnamed: 1'])
    .stack()
    .reset_index()
    .rename(columns={'Unnamed: 1':'row', 'level_1':'col', 0 :'val'})
    )

    df.to_sql('matrizinfo', conn, if_exists='append', index=False)