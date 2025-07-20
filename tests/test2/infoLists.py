from pprint import pprint
import openpyxl
import time as t
import pandas as pd
import sqlite3


if __name__ == "__main__":
    pessoas = [{'name': 'Daniel', 'email': 'flaniel.arp@gmail.com'},
           {'name': 'Darp', 'email': 'instadarp@gmail.com'},
           {'name': 'Fugi', 'email': 'ohofugii@gmail.com'},
           {'name': 'Andrei', 'email': 'Andreibfmg01@gmail.com'},
           {'name': 'Matheus', 'email': 'perdoncini1105@gmail.com'},
           {'name': 'Rian', 'email': 'rianrocha2003@gmail.com'},
           {'name': 'Pedro', 'email': 'pedrohenriquedm2208@gmail.com'},
           {'name': 'Gustavo', 'email': 'flaniel.arp@gmail.com'},
           {'name': 'Lucas', 'email': "Sem informação"}]

    df = pd.DataFrame(pessoas)
    df = df[df['email'] != 'Sem informação']
    df = df.drop_duplicates(subset=["email"], keep='first')
    df = df.reset_index(drop=True)
    df['email_enviado'] = False

    conn = sqlite3.connect('src/db/clientes_teste2.db')
    df.to_sql('clientes', conn, if_exists='replace', index=False)
    t.sleep(5)

    query = """SELECT * FROM clientes WHERE email_enviado = 0
            ORDER BY RANDOM() LIMIT 15 """
    df = pd.read_sql_query(query, conn)
    conn.close()
    pprint(df.to_dict(orient='records'))

   