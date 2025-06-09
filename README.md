
# 🧠 Analizando_EA1

Este proyecto forma parte de la Evidencia de Aprendizaje del Curso "Programación para Análisis de Datos". Tiene como objetivo aplicar técnicas de **web scraping**, estructuración de datos y automatización de flujos de desarrollo utilizando **GitHub Actions** para CI/CD y contenedores Docker.

## 📌 Descripción

Se desarrolló una aplicación que extrae información de películas desde [SensaCine](https://www.sensacine.com/), la estructura en un API con FastAPI, y la despliega utilizando contenedores Docker y automatización con GitHub Actions.

## 🎯 Objetivos

### Objetivo General
Aplicar la metodología de desarrollo DevOps mediante GitHub Actions y contenedores Docker para automatizar la recolección, análisis y despliegue de datos provenientes del portal SensaCine.

### Objetivos Específicos
- Automatizar el scraping de datos con Python y BeautifulSoup.
- Implementar una API con FastAPI para exponer los datos.
- Crear un contenedor Docker para ejecutar localmente la aplicación.
- Establecer un flujo de integración y despliegue continuo con GitHub Actions.
- Documentar detalladamente el proceso y resultados en el repositorio.
- Guardar los documentos generados en artefactos dentro de Actions y Docker Hub.
- Enviar Auditoria por correo electronico para posteriores revisiones de calidad.

## ⚙️ Instalación y uso

### Requisitos
- Docker
- Git
- Python 3.11+

### Clonar repositorio
```bash
git clone https://github.com/Lashkmy/Analizando_EA1.git
cd Analizando_EA1
```

### Construir imagen Docker
```bash
docker build -t analizando-ea1 .
```

### Ejecutar contenedor
```bash
docker run -d -p 8000:8000 analizando-ea1
```

### Acceder al API
[http://localhost:8000/movies](http://localhost:8000/movies)

## 🤖 Automatización con GitHub Actions

Se configuró un workflow en `.github/workflows/ci-cd.yml` que realiza:

- Validación de dependencias
- Pruebas automáticas
- Construcción de imagen Docker
- Despliegue (local/test)

```yaml
name: CI/CD Pipeline

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
      - name: Docker build
        run: docker build -t analizando-ea1 .
```

## 🌐 Visualizaciones

### Scraper funcionando
![Scraper output](screenshots/scraper_output.png)

### API activa en local
![API en localhost](screenshots/api_response.png)

### Ejecución exitosa del workflow
![GitHub Actions workflow](screenshots/github_actions.png)

## 📄 Estructura del proyecto

```
Analizando_EA1/
│
├── app/
│   ├── main.py        # Lógica FastAPI
│   ├── scraper.py     # Web scraping SensaCine
│   └── utils.py
│
├── tests/
│   └── test_scraper.py
│
├── Dockerfile
├── requirements.txt
├── .github/workflows/ci-cd.yml
└── README.md
```

## 📚 Bibliografía.

- Sweigart, A. (2015). *Automate the Boring Stuff with Python*. No Starch Press.
- McKinney, W. (2022). *Python for Data Analysis*. O'Reilly.
- GitHub Actions Documentation. (2024). [https://docs.github.com/en/actions](https://docs.github.com/en/actions)
- Docker Docs. (2024). [https://docs.docker.com/](https://docs.docker.com/)
- SensaCine. (2024). [https://www.sensacine.com/](https://www.sensacine.com/)
