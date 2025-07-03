# 🔐 Session Monitor for FortiGate

Skrip Python modular untuk:
- Memantau login captive portal user FortiGate
- Membatasi jumlah perangkat per user
- Mengirim notifikasi Telegram saat user melebihi limit
- Mencatat log ke SQLite
- Menampilkan dashboard riwayat login via Flask

---

## 📦 Struktur File
session-monitor/ 
├── config.py # Konfigurasi IP FortiGate, Telegram, max devices 
├── db.py # Logging ke SQLite 
├── telegram_notif.py # Kirim notifikasi ke Telegram 
├── session_monitor.py # Monitor sesi & eksekusi utama 
├── web_dashboard.py # Jalankan dashboard web lokal 
├── requirements.txt # Daftar dependensi Python
└── templates/ 
  └── dashboard.html # Template HTML dashboard

---

## 🚀 Instalasi

### 1. Clone repository
```bash
git clone https://github.com/rgunawans/session-monitor.git
cd session-monitor
pip3 install -r requirements.txt
