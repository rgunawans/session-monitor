# web_dashboard.py
# Dashboard web untuk memantau riwayat sesi user dari SQLite

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def dashboard():
    conn = sqlite3.connect("session_logs.db")
    c = conn.cursor()
    c.execute("SELECT * FROM logs ORDER BY timestamp DESC LIMIT 50")
    logs = c.fetchall()
    conn.close()
    return render_template("dashboard.html", logs=logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
