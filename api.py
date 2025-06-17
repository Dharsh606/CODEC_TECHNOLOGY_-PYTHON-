import requests
import sqlite3
import time
from datetime import datetime

# Database setup
conn = sqlite3.connect("api_monitor.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS api_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    status_code INTEGER,
    response_time REAL,
    success INTEGER,
    timestamp TEXT
)''')
conn.commit()

# Function to monitor a single API
def monitor_api(url):
    start = time.time()
    try:
        response = requests.get(url)
        duration = round(time.time() - start, 3)
        status = response.status_code
        success = 1 if status == 200 else 0
    except:
        duration = 0
        status = 0
        success = 0

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO api_logs (url, status_code, response_time, success, timestamp) VALUES (?, ?, ?, ?, ?)",
              (url, status, duration, success, timestamp))
    conn.commit()
    print(f"{timestamp} | {url} | Status: {status} | Time: {duration}s")

# Example: Add your API URL here
api_urls = [
    "https://api.openweathermap.org/data/2.5/weather?q=London&appid=your_api_key",
    "https://jsonplaceholder.typicode.com/posts"
]

# Run monitor
for url in api_urls:
    monitor_api(url)

# Close DB connection
conn.close()
