#!/usr/bin/python3
"""Run df -h through the commands in commands.json and write myfilecsv.csv."""
import json
import os

SUPPORTED = ("Ubuntu", "CentOS Stream", "Red Hat Enterprise Linux")

try:
    with open("commands.json") as jf:
        commands = json.load(jf)

    os_name = os.popen(commands["os_flavour"]).read().strip()
    if os_name in SUPPORTED:
        os.popen(commands["df_cmd"]).read()
        print("CSV file generated successfully in the current directory")
    else:
        print("Other OS found:", os_name)
except Exception as e:
    print("Something has an issue:", e)
