from setuptools import setup, find_packages


setup(
    name="Analizando_EA1",
    version="0.0.1",
    author="Indira Hamdam",
    author_email="indira.hamdam@est.iudigital.edu.co",
    description="Proyecto educativo de obtención de datos basado en Web Scraping con BeautifulSoup para extraer, procesar y visualizar información de las 250 mejores películas según IMDb.",
    py_modules=[""],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4",
    ]
)