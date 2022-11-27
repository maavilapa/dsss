# setup.py
import setuptools

setuptools.setup(
    name="snowflake",
    version="0.1",
    author="Mateo Avila",
    author_email="mateo.avila@fau.de",
    description="Exercise 5 package",
    packages=["snowflake"],
    install_requires=['turtles',
                      'numpy',                     
                      ],
)