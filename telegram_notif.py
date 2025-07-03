# telegram_notif.py
# Modul untuk mengirim notifikasi via Telegram

import requests
from config import TELEGRAM_TOKEN, CHAT_ID

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, data=data)
        if not response.ok:
            print(f"[Telegram] Gagal kirim pesan: {response.text}")
    except Exception as e:
        print(f"[Telegram] Error: {e}")
