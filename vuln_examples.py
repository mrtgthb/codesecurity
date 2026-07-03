"""
vuln_examples.py

Bu dosya, SAST (Static Application Security Testing) araçlarının
yakalaması beklenen KLASİK kod zafiyeti kalıplarını içerir.
Amaç: code security tarama testleri.

Bunlar gerçek çalışan bir uygulamaya bağlı DEĞİLDİR ve exploit
payload'u içermez; sadece "insecure pattern" örnekleridir.
Production'da KULLANMAYIN.
"""

import os
import sqlite3
import subprocess
import pickle
import hashlib


# [Finding - CWE-798] Hardcoded credentials
DB_PASSWORD = "SuperSecret123!"
API_TOKEN = "sk-sample-hardcoded-token-abcdef123456"


# [Finding - CWE-89] SQL Injection: kullanıcı girdisi doğrudan sorguya ekleniyor
def get_user(username: str):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


# [Finding - CWE-78] OS Command Injection: kullanıcı girdisi shell'e geçiriliyor
def ping_host(host: str):
    return subprocess.check_output("ping -c 1 " + host, shell=True)


# [Finding - CWE-22] Path Traversal: kullanıcı girdisiyle dosya yolu oluşturuluyor
def read_uploaded_file(filename: str):
    base_dir = "/app/uploads/"
    with open(base_dir + filename, "r") as f:
        return f.read()


# [Finding - CWE-502] Insecure Deserialization: güvenilmeyen veriden pickle.loads
def load_session(serialized_data: bytes):
    return pickle.loads(serialized_data)


# [Finding - CWE-327] Zayıf/kırık hash algoritması ile parola saklama
def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


# [Finding - CWE-489] Debug modu production'da açık bırakılmış varsayım
DEBUG_MODE = os.environ.get("DEBUG", "true")


# [Finding - CWE-798 / CWE-330] Zayıf/öngörülebilir secret key
SECRET_KEY = "changeme"
