# Log Archiver

Archives a log file into a dated `.tgz` when it reaches 1 MB, then empties it. Walkthrough: [topic 37](../../37.%20Project%20-%20Log%20Archiving%20Automation.md).

```bash
sudo python3 archive_log.py
```

Edit `LOG_FILE` and `LIMIT_MB` at the top of the script. Schedule it with cron:

```text
10 0 * * * /usr/bin/python3 /path/to/archive_log.py
```
