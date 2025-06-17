🚀 Real-Time Python Projects

This repository contains two powerful real-time Python projects:

1. 📊 Real-Time Stock Market Dashboard
2. 🚦 API Performance Monitor

Each project is designed to demonstrate live data tracking, visualization, and backend efficiency monitoring.

---

📊 Project 1: Real-Time Stock Market Dashboard

A responsive and real-time dashboard to monitor live stock prices using the Alpha Vantage API. Built with Streamlit, Pandas, and Plotly for sleek visualization.

🔧 Technologies:
- Python
- Streamlit
- Plotly
- Pandas
- Requests
- Alpha Vantage API

💡 Features:
- Live stock tracking with multiple time intervals
- Plotly-powered interactive graphs
- Latest stock price, delta change, and data table
- Clean UI with auto-refresh (every 60 sec)

📦 Installation:
pip install streamlit requests pandas plotly

▶️ Running the App:
streamlit run stock_dashboard.py
Then open your browser at: http://localhost:8501

🔐 API Key Setup:
1. Get a free API key from https://www.alphavantage.co/support/#api-key
2. Replace the "demo" key in your code:
   api_key = "your_api_key_here"

---

🚦 Project 2: API Performance Monitor

A tool to track and analyze the performance of REST APIs — logging response times, status codes, and uptime. Ideal for developers and backend testers.

🔧 Technologies:
- Python
- Requests
- SQLite
- Time / Schedule
- (Optional) Streamlit or Matplotlib for visualization

💡 Features:
- Real-time API tracking
- Logs response times and HTTP codes
- SQLite database storage
- Extendable to include analytics and dashboards

📦 Installation:
pip install requests

▶️ Running the Monitor:
python api_monitor.py

🗃️ Database Schema:
CREATE TABLE api_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    url TEXT,
    status_code INTEGER,
    response_time_ms REAL
);

🔍 Example Log Output:
2025-06-17 09:05:00 | GET https://api.example.com | Status: 200 | Time: 134 ms
2025-06-17 09:06:00 | GET https://api.example.com | Status: 500 | Time: 88 ms

---

📁 Folder Structure:
├── stock_dashboard.py         # Streamlit app for stock tracker
├── api_monitor.py             # API monitoring script
├── database.sqlite            # SQLite DB for logs
├── README.txt                 # Project documentation
├── LICENSE                    # Project license file

---

📌 License

This project is licensed under the MIT License — see the `LICENSE` file for full details.

---

🙌 Contributing

Contributions are welcome! Feel free to:
- Add new indicators or stock comparisons
- Visualize API performance trends
- Convert into a web-hosted dashboard (e.g., Streamlit Cloud)

🔗 Author:
Made with ❤️ by Dharshan V  
Connect on LinkedIn | GitHub: @yourhandle
