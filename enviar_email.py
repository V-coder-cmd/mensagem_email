import smtplib
import os
import re
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

load_dotenv()

EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
SENHA_APP = os.getenv("SENHA_APP")


def email_valido(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(padrao, email)


def registrar_log(email):
    with open("logs.txt", "a") as log:
        log.write(f"{datetime.now()} - Email enviado para {email}\n")


def enviar(email_destino):
    if not email_valido(email_destino):
        raise ValueError("Email inválido")

    mensagem = MIMEMultipart()
    mensagem["From"] = EMAIL_REMETENTE
    mensagem["To"] = email_destino
    mensagem["Subject"] = "Sistema automático de e-mail 🚀"

    html = """
    <html>
        <body>
            <h2>Olá!</h2>
            <p>Este email foi enviado automaticamente usando <b>Python</b>.</p>
            <p>Status do sistema: <span style="color:green;">OK</span></p>
        </body>
    </html>
    """

    mensagem.attach(MIMEText(html, "html"))

    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls()
        servidor.login(EMAIL_REMETENTE, SENHA_APP)
        servidor.send_message(mensagem)

    registrar_log(email_destino)
