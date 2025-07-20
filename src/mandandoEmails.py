import smtplib
import time
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import pandas as pd
import sqlite3
import json

link = "https://allblueunb.com"

with open('src/config/emailTemplates.json', 'r') as file:
    email_templates = json.load(file)

# Load email credentials from a JSON file
with open('src/config/emailConfig.json', 'r') as file:
    config = json.load(file)
    EMAIL_ADDRESS = config['EMAIL_ADDRESS']
    EMAIL_PASSWORD = config['EMAIL_PASSWORD']
    SMTP_SERVER = config['SMTP_SERVER']
    SMTP_PORT = config['SMTP_PORT']

def enviar_email(destinatario, assunto, corpo):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = destinatario
        msg['Subject'] = assunto

        msg.attach(MIMEText(corpo, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, destinatario, msg.as_string())
        
        print(f"Email enviado para {destinatario} com sucesso!")

        # Update the database to mark the email as sent
        conn = sqlite3.connect('src/db/clientes.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE clientes SET email_enviado = 1 WHERE email = ?", (destinatario,))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erro ao enviar email para {destinatario}: {e}")

def rodar_envios():
    conn = sqlite3.connect('src/db/clientes.db')
    query = """SELECT * FROM clientes WHERE email_enviado = 0 ORDER BY RANDOM() LIMIT 15"""
    df = pd.read_sql_query(query, conn)
    df = df.to_dict(orient='records')
    conn.close()
    
    clientes = df
    random.shuffle(clientes)
    for i, cliente in enumerate(clientes):
        template = random.choice(email_templates)

        assunto = template['subject']
        corpo = template['body'].format(name=cliente['name'], link=link)

        enviar_email(cliente['email'], assunto, corpo)

        if i < len(clientes) - 1:
            wait_time = random.randint(1800, 7200) 
            print(f"Aguardando {wait_time} segundos antes de enviar o próximo email...")
            time.sleep(wait_time)

