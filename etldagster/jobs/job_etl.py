from dagster import job
from etldagster.ops.etl import load_table

@job
def matriz_data():
    load_table()
