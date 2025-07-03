# config.py
# Konfigurasi utama untuk session monitor

# FortiGate Credentials
FORTIGATE_IP = "192.168.1.99"        # Ganti dengan IP FortiGate kamu
USERNAME = "admin"                   # Username FortiGate
PASSWORD = "your-password"           # Password FortiGate

# Batas maksimal device per user
MAX_DEVICES = 2

# Telegram Bot Integration
TELEGRAM_TOKEN = "your_bot_token_here"   # Dapatkan dari @BotFather
CHAT_ID = "your_chat_id_here"            # ID admin yang akan menerima notifikasi
