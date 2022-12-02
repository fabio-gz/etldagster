from setuptools import find_packages, setup

setup(
    name="etldagster",
    packages=find_packages(exclude=["etldagster_tests"]),
    install_requires=[
        "dagster",
        "pandas",
        "psycopg2",
        "configparser",
        "openpyxl"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
