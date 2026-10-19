<div align="center">

# 🐍 Python Scripting and Automation for AI and DevOps Engineering

**Automate servers the way DevOps and AI engineers do: 37 hands-on topics taking you from your first script to the os and sys modules, files, JSON and CSV, email alerts, scheduling, regex, SSH automation with Paramiko, MySQL and two real-world automation projects.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Ubuntu%20%7C%20RHEL-FCC624?logo=linux&logoColor=black)
![Paramiko](https://img.shields.io/badge/SSH-Paramiko-1D63ED)
![MySQL](https://img.shields.io/badge/MySQL-Automation-4479A1?logo=mysql&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Advanced-6D4AE0)

</div>

---

## 🎯 About this course

Practical Python automation notes. Every topic shows the script, the command and the terminal output, and most end with a task and its solution. The examples are the everyday jobs of a DevOps or AI engineer: checking disks and memory, parsing logs, reading server inventories, sending alerts and loading reports into a database.

---

## 📚 Course contents

### 🐍 Python Fundamentals

| # | Topic |
|---|---|
| 01 | [Introduction to Python and Running Scripts](01.%20Introduction%20to%20Python%20and%20Running%20Scripts.md) |
| 02 | [Variables and Data Types](02.%20Variables%20and%20Data%20Types.md) |
| 03 | [Type Casting and Print Formatting](03.%20Type%20Casting%20and%20Print%20Formatting.md) |
| 04 | [Escape Sequences and Comments](04.%20Escape%20Sequences%20and%20Comments.md) |
| 05 | [Conditional Statements](05.%20Conditional%20Statements.md) |

### 🧱 Data Structures

| # | Topic |
|---|---|
| 06 | [String Operations](06.%20String%20Operations.md) |
| 07 | [Lists and Sets](07.%20Lists%20and%20Sets.md) |
| 08 | [Tuples](08.%20Tuples.md) |
| 09 | [Dictionaries](09.%20Dictionaries.md) |

### 🖥️ Modules and the Operating System

| # | Topic |
|---|---|
| 10 | [Modules and pip](10.%20Modules%20and%20pip.md) |
| 11 | [The os Module](11.%20The%20os%20Module.md) |
| 12 | [Running Shell Commands and Walking Directories](12.%20Running%20Shell%20Commands%20and%20Walking%20Directories.md) |
| 13 | [Working with Paths using os.path](13.%20Working%20with%20Paths%20using%20os.path.md) |
| 14 | [The platform Module](14.%20The%20platform%20Module.md) |
| 15 | [Command-Line Arguments with sys](15.%20Command-Line%20Arguments%20with%20sys.md) |

### 🔁 Loops and Control Flow

| # | Topic |
|---|---|
| 16 | [for and while Loops](16.%20for%20and%20while%20Loops.md) |
| 17 | [break, continue and pass](17.%20break%2C%20continue%20and%20pass.md) |
| 18 | [Practice Set 1 with Solutions](18.%20Practice%20Set%201%20with%20Solutions.md) |
| 19 | [List and Dictionary Comprehensions](19.%20List%20and%20Dictionary%20Comprehensions.md) |

### 🧩 Functions and Errors

| # | Topic |
|---|---|
| 20 | [Functions](20.%20Functions.md) |
| 21 | [Exception Handling](21.%20Exception%20Handling.md) |

### ⏱️ Dates and Times

| # | Topic |
|---|---|
| 22 | [The datetime Module](22.%20The%20datetime%20Module.md) |
| 23 | [strftime, strptime and the time Module](23.%20strftime%2C%20strptime%20and%20the%20time%20Module.md) |

### 📂 Files and Data Formats

| # | Topic |
|---|---|
| 24 | [Reading and Writing Text Files](24.%20Reading%20and%20Writing%20Text%20Files.md) |
| 25 | [Working with JSON](25.%20Working%20with%20JSON.md) |
| 26 | [Working with CSV](26.%20Working%20with%20CSV.md) |

### 📧 Alerts and Scheduling

| # | Topic |
|---|---|
| 27 | [Sending Emails with smtplib](27.%20Sending%20Emails%20with%20smtplib.md) |
| 28 | [Scheduling Tasks](28.%20Scheduling%20Tasks.md) |

### 🔍 Regular Expressions

| # | Topic |
|---|---|
| 29 | [Regular Expressions - findall and Character Classes](29.%20Regular%20Expressions%20-%20findall%20and%20Character%20Classes.md) |
| 30 | [Regular Expressions - Quantifiers and Flags](30.%20Regular%20Expressions%20-%20Quantifiers%20and%20Flags.md) |
| 31 | [Regular Expressions - finditer, search, match, split and sub](31.%20Regular%20Expressions%20-%20finditer%2C%20search%2C%20match%2C%20split%20and%20sub.md) |

### 🌐 Remote Servers over SSH

| # | Topic |
|---|---|
| 32 | [Remote Commands over SSH with Paramiko](32.%20Remote%20Commands%20over%20SSH%20with%20Paramiko.md) |
| 33 | [File Transfers with Paramiko SFTP](33.%20File%20Transfers%20with%20Paramiko%20SFTP.md) |

### 🗄️ Databases

| # | Topic |
|---|---|
| 34 | [MySQL Setup and SQL Basics](34.%20MySQL%20Setup%20and%20SQL%20Basics.md) |
| 35 | [Python and MySQL with mysql-connector](35.%20Python%20and%20MySQL%20with%20mysql-connector.md) |

### 🚀 Real-World Projects

| # | Topic |
|---|---|
| 36 | [Project - Disk Usage Reports into MySQL](36.%20Project%20-%20Disk%20Usage%20Reports%20into%20MySQL.md) |
| 37 | [Project - Log Archiving Automation](37.%20Project%20-%20Log%20Archiving%20Automation.md) |

### 🧪 Projects and sample data

| Folder | Contents |
|---|---|
| [`projects/disk-usage-to-mysql`](projects/disk-usage-to-mysql) | df -h to CSV to MySQL pipeline with an encrypted password (topic 36) |
| [`projects/log-archiver`](projects/log-archiver) | Size-based log archiving script for cron (topic 37) |
| [`data`](data) | Sample CSV and JSON files used in topics 25 and 26 |

---

## 🚀 How to use it

1. Use a Linux machine or VM (Ubuntu or RHEL) with Python 3: `python3 --version`.
2. Work through the topics in order. Write each script with `vim <name>.py` and run it with `python3 <name>.py`, then compare your output with the one shown.
3. Install packages when a topic needs them: `pip install pytz schedule paramiko mysql-connector-python cryptography`.
4. Topics 27, 32 to 36 need a Gmail app password, a second Linux server and MySQL. The scripts read every password from environment variables (`GMAIL_APP_PASSWORD`, `SSH_PASSWORD`, `MYSQL_PASSWORD`), never from the code.

---

## 👨‍🏫 About the author

**Ahmad Hassan** | AI/ML Engineer & Instructor with 5+ years of experience
1,500+ hours of live teaching, 100+ students mentored from medicine, business and engineering into data and DevOps roles.

[![Portfolio](https://img.shields.io/badge/Portfolio-ahmadhassan--aiops.github.io-0EA5A4)](https://ahmadhassan-aiops.github.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ahmad%20Hassan-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ahmad-hassan-79a44b1a3)
[![GitHub](https://img.shields.io/badge/GitHub-ahmadhassan--aiops-181717?logo=github&logoColor=white)](https://github.com/ahmadhassan-aiops)

⭐ If these notes help you automate with Python, please star the repo. It helps other students find it!
