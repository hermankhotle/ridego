from setuptools import setup, find_packages

setup(
    name="ridego-sdk",
    version="0.1.0",
    description="Shared SDK for RideGo platform",
    packages=find_packages(),
    install_requires=[
        "pydantic==2.5.0",
        "sqlalchemy==2.0.23",
        "psycopg2-binary==2.9.9",
    ],
)
