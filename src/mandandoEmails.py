import smtplib
import time
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

link = "https://allblueunb.com"

pessoas = [{'name': 'Daniel', 'email': 'flaniel.arp@gmail.com'},
           {'name': 'Darp', 'email': 'instadarp@gmail.com'},
           {'name': 'Fugi', 'email': 'ohofugii@gmail.com'},
           {'name': 'Andrei', 'email': 'Andreibfmg01@gmail.com'},
           {'name': 'Matheus', 'email': 'perdoncini1105@gmail.com'},
           {'name': 'Rian', 'email': 'rianrocha2003@gmail.com'},
           {'name': 'Pedro', 'email': 'pedrohenriquedm2208@gmail.com'}]

email_templates = [{'subject': 'Welcome!', 'body': 'Hello {name}, welcome to our service! {link}'},
                   {'subject': 'Reminder', 'body': 'Hi {name}, just a reminder about us {link}'},
                   {'subject': 'Update', 'body': 'Dear {name}, we have an update {link} for you'}]

#Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'testeprojetoemail@gmail.com'
EMAIL_PASSWORD = 'vngy udwe chjp kdjo'

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
    except Exception as e:
        print(f"Erro ao enviar email para {destinatario}: {e}")

def main():
    random.shuffle(pessoas)
    for i, pessoa in enumerate(pessoas):
        template = random.choice(email_templates)

        assunto = template['subject']
        corpo = template['body'].format(name=pessoa['name'], link=link)

        enviar_email(pessoa['email'], assunto, corpo)

        if i < len(pessoas) - 1:
            wait_time = random.randint(60, 180)
            print(f"Aguardando {wait_time} segundos antes de enviar o próximo email...")
            time.sleep(wait_time)

if __name__ == "__main__":
    main()
    print("Todos os emails foram enviados com sucesso!")
