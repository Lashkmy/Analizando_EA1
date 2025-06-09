import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
# load_dotenv()

class SensaCineScraper:
    
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/122.0.0.0 Safari/537.36'
        }
        self.peliculas = []

    def solicitar_pagina(self):
        print(f"Solicitando página: {self.url}")
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            print("Respuesta exitosa (200 OK)")
            return response.text
        else:
            print(f"Error al hacer la solicitud: Código {response.status_code}")
            response.raise_for_status()

    def analizar_pagina(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        tarjetas = soup.find_all('div', class_='card entity-card entity-card-list cf')
        print(f" Películas encontradas: {len(tarjetas)}")

        for tarjeta in tarjetas:
            titulo = tarjeta.find('a', class_='meta-title-link').get_text(strip=True)
            enlace = 'https://www.sensacine.com' + tarjeta.find('a', class_='meta-title-link')['href']
            detalles = tarjeta.find('div', class_='meta-body-info').get_text(strip=True)
            puntuacion = tarjeta.find('span', class_='stareval-note').get_text(strip=True)

            self.peliculas.append({
                'Título': titulo,
                'Detalles': detalles,
                'Puntuación': puntuacion,
                'Enlace': enlace
            })

    def obtener_dataframe(self):
        return pd.DataFrame(self.peliculas)

    def guardar_csv(self, nombre_archivo):
        df = self.obtener_dataframe()
        df.to_csv(nombre_archivo, index=False, encoding='utf-8-sig')
        print(f"CSV guardado como: {nombre_archivo}")

    def guardar_excel(self, nombre_archivo):
        df = self.obtener_dataframe()
        df.to_excel(nombre_archivo, index=False, engine='openpyxl')
        print(f"Excel guardado como: {nombre_archivo}")

    def ejecutar(self):
        html = self.solicitar_pagina()
        self.analizar_pagina(html)
    

    def enviar_auditoria_email(self):
        smtp_server = os.getenv("SMTP_SERVER")
        smtp_port = int(os.getenv("SMTP_PORT", 587))
        email_sender = os.getenv("EMAIL_SENDER")
        email_password = os.getenv("EMAIL_PASSWORD")
        email_receiver = os.getenv("EMAIL_RECEIVER")

        print(f"SMTP_SERVER={smtp_server}")
        print(f"SMTP_PORT={smtp_port}")
        print(f"EMAIL_SENDER={email_sender}")
        print(f"EMAIL_RECEIVER={email_receiver}")

        csv_path = "static/mejores_peliculas.csv"

        msg = EmailMessage()
        msg["Subject"] = "Auditoría: Scraper ejecutado correctamente"
        msg["From"] = email_sender
        msg["To"] = email_receiver
        msg.set_content("Adjunto encontrarás el reporte de las mejores películas generado por el scraper.")

        with open(csv_path, "rb") as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype="text", subtype="csv", filename="mejores_peliculas.csv")

        try:
            if smtp_port == 465:
                with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                    server.login(email_sender, email_password)
                    server.send_message(msg)
            else:
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login(email_sender, email_password)
                    server.send_message(msg)
            print(" Email enviado con éxito.")
        except ConnectionRefusedError:
            print(" No se pudo conectar al servidor SMTP: conexión rechazada.")
        except smtplib.SMTPAuthenticationError:
            print(" Error de autenticación SMTP: revisa usuario y contraseña.")
        except Exception as e:
            print(f" Error inesperado al enviar el email: {e}")

    

# Uso de la clase SensaCineScraper.
if __name__ == "__main__":
    scraper = SensaCineScraper('https://www.sensacine.com/peliculas/mejores-peliculas/')
    scraper.ejecutar()

    df = scraper.obtener_dataframe()
    print("\n Mejores Peliculas obtenidas:")
    print(df)

    ruta_base = Path(__file__).resolve().parent
    ruta_static = ruta_base.parent / "static"

    ruta_csv = ruta_static / "mejores_peliculas.csv"
    ruta_excel = ruta_static / "mejores_peliculas.xlsx"

    scraper.guardar_csv(str(ruta_csv))
    scraper.guardar_excel(str(ruta_excel))
    
    scraper.enviar_auditoria_email()

    



