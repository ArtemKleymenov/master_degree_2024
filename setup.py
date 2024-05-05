# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Face Recognition Service - OpenAPI 3.0",
    author_email="m1801083@edu.misis.ru",
    url="",
    keywords=["Swagger", "Face Recognition Service - OpenAPI 3.0"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    This is a service for face detection and recognition. The service was created for obtaining a master&#x27;s degree at NUST MISIS in the spring of 2024. Server based on the OpenAPI 3.0 specification.  Some useful links: - [The Facial Recognition Service repository](https://github.com/swagger-api/swagger-petstore)
    """
)
