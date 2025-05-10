import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def scrape_imdb_top_250():
    url = 'https://www.imdb.com/chart/top/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception('Error al acceder a IMDb')

    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.select('tbody.lister-list tr')

    titles, years, ratings = [], [], []

    for row in rows:
        title_column = row.find('td', class_='titleColumn')
        title = title_column.a.text
        year = title_column.span.text.strip('()')
        rating = row.find('td', class_='ratingColumn imdbRating').strong.text

        titles.append(title)
        years.append(int(year))
        ratings.append(float(rating))

    df = pd.DataFrame({
        'Title': titles,
        'Year': years,
        'Rating': ratings
    })

    os.makedirs('../data', exist_ok=True)
    df.to_csv('../data/imdb_top_250.csv', index=False)
    print("Datos guardados en ../data/imdb_top_250.csv")

if __name__ == "__main__":
    scrape_imdb_top_250()
