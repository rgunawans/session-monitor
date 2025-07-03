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
git clone https://github.com/rgunawans/session-monitor.git
cd session-monitor
pip3 install -r requirements.txt

----
sudo nano /etc/systemd/system/session_monitor.service


[Unit]
Description=FortiGate Session Monitor
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/robby/session-monitor/session_monitor.py
WorkingDirectory=/home/robby/session-monitor
Restart=always
RestartSec=10
User=robby

[Install]
WantedBy=multi-user.target

---
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable session_monitor
sudo systemctl start session_monitor

---
sudo systemctl status session_monitor
journalctl -u session_monitor -f

---
sudo nano /etc/systemd/system/session_dashboard.service

---

[Unit]
Description=FortiGate Session Dashboard
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/robby/session-monitor/web_dashboard.py
WorkingDirectory=/home/robby/session-monitor
Restart=always
RestartSec=10
User=robby

[Install]
WantedBy=multi-user.target


---
sudo systemctl daemon-reload
sudo systemctl enable session_dashboard
sudo systemctl start session_dashboard

---
sudo ufw allow 8080/tcp

---
sudo nano /etc/systemd/system/session_dashboard.service
---
[Unit]
Description=FortiGate Session Dashboard
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/robby/session-monitor/web_dashboard.py
WorkingDirectory=/home/robby/session-monitor
Restart=always
RestartSec=10
User=robby

[Install]
WantedBy=multi-user.target

---
sudo systemctl daemon-reload
sudo systemctl enable session_dashboard
sudo systemctl start session_dashboard

---
sudo systemctl status session_dashboard




