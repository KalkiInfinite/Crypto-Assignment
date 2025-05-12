import streamlit as st
import numpy as np
import pandas as pd
import time
from sklearn.linear_model import LinearRegression

# Page config
st.set_page_config(page_title="Live Crypto Trade Simulator", layout="wide")

# Inject CSS for custom look
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
        }
        .stButton>button {
            background-color: #facc15;
            color: black;
            font-weight: 600;
            border-radius: 10px;
            padding: 0.5em 1em;
        }
        .stTextInput>div>div>input {
            background-color: #1e1e1e !important;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Inputs
with st.sidebar:
    st.markdown("## Trade Input Parameters")
    asset = st.selectbox("Asset", ["BTC-USDT"])
    order_type = st.selectbox("Order Type", ["Market"])
    order_size_usd = st.slider("Order Size (USD)", min_value=10, max_value=300, value=50, step=10)
    fee_tier = st.selectbox("Fee Tier", ["Tier 1", "Tier 2", "Tier 3"])
    volatility = st.slider("Volatility (sampled)", min_value=0.00, max_value=0.10, value=0.02, step=0.01)
    simulate = st.button("Simulate Trade")

# Models
def almgren_chriss_market_impact(order_size, daily_volume=50000000, volatility=0.02, eta=0.142, gamma=2.5e-6):
    sigma = volatility
    q = order_size
    Q = daily_volume
    permanent = gamma * q / Q
    temporary = eta * (q / Q) ** 0.5
    return permanent + temporary

def predict_slippage(order_size):
    X = np.array([[10], [50], [100], [200], [300]])
    y = np.array([0.01, 0.04, 0.07, 0.13, 0.18])
    model = LinearRegression().fit(X, y)
    return model.predict(np.array([[order_size]]))[0]

def maker_taker_proportion_prediction(order_type):
    return 0.6 if order_type == "Limit" else 0.1

# Main Content
st.markdown("# Live Crypto Trade Simulator")
st.markdown("### Live Orderbook Data + Trade Cost Analysis")
st.markdown("---")

if simulate:
    start_time = time.time()
    market_price = 30000.0
    market_impact = almgren_chriss_market_impact(order_size_usd, volatility=volatility)
    slippage = predict_slippage(order_size_usd)
    avg_execution_price = market_price + (market_impact + slippage) * market_price
    fee_rate = {"Tier 1": 0.001, "Tier 2": 0.002, "Tier 3": 0.003}[fee_tier]
    fees = order_size_usd * fee_rate
    net_cost = (avg_execution_price - market_price) + fees
    latency = (time.time() - start_time) * 1000

    # Layout
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("## Simulation Results")
        st.text_input("Average Execution Price", f"${avg_execution_price:.2f}", disabled=True)
        st.text_input("Slippage", f"${slippage * market_price:.2f}", disabled=True)
        st.text_input("Estimated Fees", f"${fees:.2f}", disabled=True)

    with col2:
        st.markdown("## ")
        st.text_input("Market Impact", f"${market_impact * market_price:.2f}", disabled=True)
        st.text_input("Net Cost", f"${net_cost:.2f}", disabled=True)
        st.text_input("Processing Latency", f"{latency:.2f} ms", disabled=True)
