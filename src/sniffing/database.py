import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "blacklist.db")

def setup_database():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ftp_attempts(
            ip_address TEXT,
            username TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS nmap_attempts(
            ip_address TEXT,
            type TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")


def add_to_databaseFTP(ip_address, username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO ftp_attempts(ip_address, username) VALUES(?, ?)", (ip_address, username))
    
    conn.commit()
    conn.close()

def add_to_databaseNMAP(ip_address,type):
     conn = sqlite3.connect(DB_NAME)
     cursor = conn.cursor()
     cursor.execute("INSERT INTO nmap_attempts(ip_address,type) VALUES(?, ?)", (ip_address,type))
     conn.commit()
     conn.close()

