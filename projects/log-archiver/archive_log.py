#!/usr/bin/python3
"""Archive a log file into a dated .tgz when it reaches a size limit."""
import os
import tarfile
from datetime import date

LOG_FILE = "/var/log/syslog"          # on RHEL/CentOS: /var/log/messages
LIMIT_MB = 1.0

today = date.today().strftime("%d%B%Y")
file_mb = os.stat(LOG_FILE).st_size / 1_000_000
print(today)
print(f"{file_mb} MB")

if file_mb >= LIMIT_MB:
    print("File is huge, proceeding to archive")
    archive_path = f"{LOG_FILE}_{today}.tgz"
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(LOG_FILE)
    open(LOG_FILE, "w").close()       # empty the log, keep the file and its permissions
    print(f"Archive created: {archive_path}")
else:
    print("File is small")
