"""Run once: encrypt the MySQL password and save it with its key."""
import getpass
import json
import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("secret.key", "wb") as kf:
    kf.write(key)
os.chmod("secret.key", 0o600)

password = getpass.getpass("MySQL password for mysql_user: ")
token = Fernet(key).encrypt(password.encode("utf-8")).decode("utf-8")

config = {"host": "192.168.1.8", "user": "mysql_user", "password": token, "database": "cloudops"}
with open("db.json", "w") as jf:
    json.dump(config, jf, indent=4)

print("Saved db.json and secret.key")
