from dagster import schedule
from etldagster.jobs.job_etl import matriz_data

@schedule(
    cron_schedule="0 10 * * *",
    job=matriz_data,
    execution_timezone="America/Bogota"
)
def etl_schedule():
    run_config = {}
    return run_config