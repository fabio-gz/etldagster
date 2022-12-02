from dagster import load_assets_from_package_module, repository

from etldagster import assets
from etldagster.ops.etl import load_table
from etldagster.jobs.job_etl import matriz_data
from etldagster.schedules.sched import etl_schedule

@repository
def etldagster():
    return [matriz_data, etl_schedule]
