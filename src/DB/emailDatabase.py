import sqlite3
from datetime import datetime
from emailSender.config import INTERVALOS

class EmailDatabase:
    def __init__(self, db_path='emails.db'):
        self.conn = sqlite3.connect(db_path)
        self._initDb()
    
    def _initDb(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT,
                          company TEXT,
                          email TEXT UNIQUE,
                          occupation TEXT,
                          send_email BOOLEAN DEFAULT 0,
                          sent_time DATETIME,
                          attempts INTEGER DEFAULT 0,
                          last_error TEXT,
                          custom_fields TEXT)''')
        self.conn.commit()
    
    def add_contact(self, contact):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM contacts 
                         WHERE send_email = 0 AND attempts < ?
                         ORDER BY RANDOM()
                         LIMIT ?''',
                     (INTERVALOS['max_attempts'], INTERVALOS['daily_limit']))
        return cursor.fetchall()
    
    def mandado_email(self, contact_id, error):
        cursor = self.conn.cursor()
        cursor.execute('''UPDATE contacts 
                        SET attempts = attempts + 1,
                            last_error = ?
                        WHERE id = ?''',
                     (str(error)[:200], contact_id))
        self.conn.commit()
    
    def get_stats(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT 
                         SUM(send_email) as sent,
                         SUM(CASE WHEN send_email = 0 AND attempts = 0 THEN 1 ELSE 0 END) as pending,
                         SUM(CASE WHEN send_email = 0 AND attempts > 0 THEN 1 ELSE 0 END) as failed,
                         COUNT(*) as total
                         FROM contacts''')
        return dict(zip(('sent', 'pending', 'failed', 'total'), cursor.fetchone()))
    
    def close(self):
        self.conn.close()