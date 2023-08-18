import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "blacklist.db")

def setup_database():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS attempts(
            ip_address TEXT,
            username TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")


def add_to_database(ip_address, username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO attempts(ip_address, username) VALUES(?, ?)", (ip_address, username))
    
    conn.commit()
    conn.close()
