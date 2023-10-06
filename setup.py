from setuptools import find_packages, setup

setup(
    name="ducker",
    packages=find_packages(exclude=["ducker_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "pandas",
        "duckdb",
        "sqlescapy",
        "lxml",
        "html5lib",
        "localstack",
        "awscli",
        "awscli-local"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
