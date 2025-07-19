#STMP configuration
SMTP_CONFIG = {
    'server': 'smtp.gmail.com',
    'port': 587,
    'email': 'testeprojeto@gmail.com',
    'password': 'vngy udwe chjp kdjo',
    'signature': 'All Blue UNB\nhttps://allblueunb.com'
    }

# Intervalos de envio
INTERVALOS = {
    'limite': 15,
    'min_delay': 1800, #30 minutos
    'max_delay': 7200, #2 horas
    'max-tentativas': 3,
    'timezone' : 'UTC'
    }


class Template_Email:
    def __init__(self, name):
        self.name = name
    
    def setSubject(self):
        self.subject = input(f"Digite o assunto do email para {self.name}: ")
    
    def setBody(self):
        self.body = input(f"Digite o corpo do email para {self.name}: ")
    
    def getSubject(self):
        self.setSubject() = 