import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.sensacine.com/peliculas/mejores-peliculas/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/122.0.0.0 Safari/537.36'
}

print(f"Solicitando página: {url}")
response = requests.get(url, headers=headers)

# Verificación explícita del estado de la respuesta
if response.status_code == 200:
    print(" Respuesta exitosa (200 OK)")
else:
    print(f"Error al hacer la solicitud: Código {response.status_code}")
    response.raise_for_status()  # Esto lanzará una excepción si no fue 200

soup = BeautifulSoup(response.text, 'html.parser')
peliculas = soup.find_all('div', class_='card entity-card entity-card-list cf')

print(f"🎬 Películas encontradas: {len(peliculas)}")

datos_peliculas = []

for pelicula in peliculas:
    titulo = pelicula.find('a', class_='meta-title-link').get_text(strip=True)
    enlace = 'https://www.sensacine.com' + pelicula.find('a', class_='meta-title-link')['href']
    detalles = pelicula.find('div', class_='meta-body-info').get_text(strip=True)
    puntuacion = pelicula.find('span', class_='stareval-note').get_text(strip=True)
    
    datos_peliculas.append({
        'Título': titulo,
        'Detalles': detalles,
        'Puntuación': puntuacion,
        'Enlace': enlace
    })

df = pd.DataFrame(datos_peliculas)
print(df.head(10))