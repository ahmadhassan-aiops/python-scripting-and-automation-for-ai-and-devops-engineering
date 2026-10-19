# Disk Usage Reports into MySQL

Collects `df -h` from a Linux server, saves it as CSV and imports it into MySQL. Walkthrough: [topic 36](../../36.%20Project%20-%20Disk%20Usage%20Reports%20into%20MySQL.md).

| File | Purpose |
|---|---|
| `commands.json` | The shell commands: OS check and the `df -h` to CSV pipeline |
| `collect_df.py` | Runs the commands and writes `myfilecsv.csv` |
| `schema.sql` | Creates the `my_df_data` table |
| `encrypt_password.py` | Run once: saves the encrypted MySQL password (`db.json`) and its key (`secret.key`) |
| `load_to_mysql.py` | Generates the CSV and imports it into MySQL |

## Run

```bash
pip install mysql-connector-python cryptography
mysql -u mysql_user -p cloudops < schema.sql
python3 encrypt_password.py
python3 load_to_mysql.py
```

`secret.key`, `db.json` and the generated CSV are ignored by Git.
