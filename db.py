# db.py
# Modul untuk menyimpan log sesi user ke SQLite

import sqlite3

def log_to_db(user, ip, status):
    conn = sqlite3.connect("session_logs.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            timestamp TEXT,
            username TEXT,
            ip TEXT,
            status TEXT
        )
    ''')
    c.execute("INSERT INTO logs VALUES (datetime('now'), ?, ?, ?)", (user, ip, status))
    conn.commit()
    conn.close()
