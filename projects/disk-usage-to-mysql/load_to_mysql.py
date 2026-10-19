#!/usr/bin/python3
"""Generate myfilecsv.csv, then import it into the my_df_data table."""
import csv
import json
import os
import mysql.connector
from cryptography.fernet import Fernet

try:
    print("Running collect_df.py to create the CSV file...")
    os.system("python3 collect_df.py")

    print("Reading the MySQL settings and decrypting the password...")
    with open("secret.key", "rb") as kf:
        key = kf.read()
    with open("db.json") as jf:
        db = json.load(jf)
    password = Fernet(key).decrypt(db["password"].encode("utf-8")).decode("utf-8")

    mydb = mysql.connector.connect(host=db["host"], user=db["user"],
                                   password=password, database=db["database"])

    print("Reading the CSV file and storing it in MySQL...")
    with open("myfilecsv.csv") as csv_file:
        all_values = [tuple(row[:9]) for row in csv.reader(csv_file)]

    query = ("insert into my_df_data (filesystem,size,used,avail,usage_with_per,"
             "mounted_on,datetime,ip_address,hostname) "
             "values (%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    cursor = mydb.cursor()
    cursor.executemany(query, all_values)
    mydb.commit()
    print(cursor.rowcount, "rows imported into the database successfully")
    mydb.close()
except Exception as e:
    print("Something has an issue:", e)
