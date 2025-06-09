import smtplib
from email.message import EmailMessage
import getpass

def enviar_email():
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    email_sender = input("Correo remitente (gmail completo): ").strip()
    email_password = "orlexrdceuumnclw"
    email_receiver = input("Correo destinatario: ").strip()

    msg = EmailMessage()
    msg['Subject'] = "Prueba SMTP simple"
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg.set_content("Esto es un correo de prueba enviado con SMTP y app password.")

    try:
        print("Conectando a SMTP...")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            print("Iniciando STARTTLS...")
            server.starttls()
            server.ehlo()
            print("Iniciando sesión...")
            server.login(email_sender, email_password)
            print("Enviando correo...")
            server.send_message(msg)
        print("Correo enviado con éxito ✅")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Error de autenticación SMTP: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    enviar_email()