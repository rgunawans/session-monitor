# session_monitor.py
# Skrip utama untuk memantau sesi login FortiGate, membatasi perangkat, kirim notifikasi, dan logging ke SQLite

import paramiko
import re
from collections import defaultdict
from config import FORTIGATE_IP, USERNAME, PASSWORD, MAX_DEVICES
from telegram_notif import send_telegram_alert
from db import log_to_db

def get_auth_list(ssh_client):
    stdin, stdout, _ = ssh_client.exec_command("diagnose firewall auth list")
    return stdout.read().decode()

def parse_sessions(output):
    users = defaultdict(list)
    current_user = None
    for line in output.splitlines():
        if "user name" in line:
            match = re.search(r"user name\s+:\s+(\S+)", line)
            if match:
                current_user = match.group(1)
        elif "IP" in line and current_user:
            ip_match = re.search(r"IP\s+:\s+(\d+\.\d+\.\d+\.\d+)", line)
            if ip_match:
                users[current_user].append(ip_match.group(1))
    return users

def clear_session(ssh_client, ip):
    ssh_client.exec_command(f"diagnose firewall iprope clear {ip}")

def main():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(FORTIGATE_IP, username=USERNAME, password=PASSWORD)

    output = get_auth_list(ssh)
    sessions = parse_sessions(output)

    for user, ips in sessions.items():
        if len(ips) > MAX_DEVICES:
            alert_msg = f"🚨 User <b>{user}</b> login dari {len(ips)} perangkat! Melebihi batas {MAX_DEVICES}.\n📍 IP yang ditendang: {', '.join(ips[:-MAX_DEVICES])}"
            send_telegram_alert(alert_msg)
            for ip in ips[:-MAX_DEVICES]:
                clear_session(ssh, ip)
                log_to_db(user, ip, "KICKED")
        else:
            for ip in ips:
                log_to_db(user, ip, "ALLOWED")

    ssh.close()

if __name__ == "__main__":
    main()
