import streamlit as st
import pandas as pd
import requests
import plotly.graph_objs as go
from datetime import datetime

st.set_page_config(page_title="📈 Real-Time Stock Tracker", layout="centered")

# === Sidebar Input ===
st.sidebar.header("Stock Dashboard Settings")
api_key = "TK9485DMFITKP5VI"  # Use your own Alpha Vantage API key
symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL)", "AAPL").upper()
interval = st.sidebar.selectbox("Interval", ["1min", "5min", "15min", "30min", "60min"], index=1)

# === Fetch Stock Data ===
@st.cache_data(ttl=60)  # Auto-refresh every 60 seconds
def fetch_data(symbol, interval):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY" \
          f"&symbol={symbol}&interval={interval}&apikey={api_key}&outputsize=compact"
    response = requests.get(url).json()

    try:
        data = response[f"Time Series ({interval})"]
    except:
        return None

    df = pd.DataFrame(data).T
    df.columns = ["Open", "High", "Low", "Close", "Volume"]
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)
    return df

# === Display Data ===
df = fetch_data(symbol, interval)

st.title("📊 Real-Time Stock Market Dashboard")
st.write(f"Showing real-time data for **{symbol}** every **{interval}** interval.")

if df is not None:
    latest = df.iloc[-1]
    st.metric(label="Latest Price", value=f"${latest['Close']:.2f}", delta=f"{latest['Close'] - latest['Open']:.2f}")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df["Close"], mode="lines+markers", name="Close"))
    fig.update_layout(title=f"{symbol} Stock Price", xaxis_title="Time", yaxis_title="Price (USD)", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Recent Data Table")
    st.dataframe(df.tail(10))

else:
    st.error("Failed to fetch stock data. Check your symbol or API limit.")

