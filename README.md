# etldagster

This is a [Dagster](https://dagster.io/) project scaffolded with [`dagster project scaffold`](https://docs.dagster.io/getting-started/create-new-project).
This project aims to create an ETL with the orchestrator tool Dagster. One simple job to retrive information from a Excel file and load it into a Postgres database.

## Database schema

There is just one table that stores the data from a matrix in an Excel file
The matrix was stacked to be represented in a relational table with 3 columns, **row**, **col** and **val**
row and col columns are the compound keys

## Transformations

The data from the matrix was transformed using the pandas library, the file was read with read_excel function and stacked with the stack function

## Orchestration

Within Dagster an ops was created to make the database operations and data transformation
The job took this operation and the schedule set a daily run at 10am

## Getting started

First, install your Dagster repository as a Python package. By using the --editable flag, pip will install your repository in ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs) so that as you develop, local code changes will automatically apply.

```bash
pip install -e ".[dev]"
```

Then, start the Dagit web server:

```bash
dagit
```

Open http://localhost:3000 with your browser to see the project.

You can start writing assets in `etldagster/assets/`. The assets are automatically loaded into the Dagster repository as you define them.

