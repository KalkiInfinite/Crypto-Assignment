# Live Crypto Trade Simulator

A real-time crypto trade simulator built with **Streamlit**, integrating live orderbook data and financial models to analyze execution metrics such as **average execution price**, **slippage**, **fees**, **market impact**, and **latency**.

---

## Features

- **Real-time WebSocket Orderbook Integration**
- **Almgren-Chriss Market Impact Model**
- **Slippage Prediction using Regression**
- **Maker/Taker Fee Tier Analysis**
- **Customizable Trade Parameters**
- **Detailed Cost Metrics Visualization**

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/crypto-trade-simulator.git
cd crypto-trade-simulator
pip install -r requirements.txt
```

Launch the Streamlit app:

```bash
streamlit run app.py
```

---

## Model Overview

| Component                    | Model Used             | Description                                                  |
|-----------------------------|------------------------|--------------------------------------------------------------|
| Market Impact               | Almgren-Chriss         | Predicts permanent and temporary price impacts               |
| Slippage Estimation         | Linear Regression      | Based on order size, volatility, order type, fee tier        |
| Fee Computation             | Rule-based Logic       | Maker vs Taker fee impact based on exchange fee tiers        |

---

## Trade Input Parameters

- **Asset** (e.g., BTC/USDT)
- **Order Type** (Market / Limit)
- **Order Size** (USD)
- **Volatility** (simulated)
- **Fee Tier** (Tier 1, 2, 3...)

---

## Simulation Outputs

- **Average Execution Price**
- **Slippage**
- **Market Impact**
- **Estimated Fees**
- **Net Cost**
- **Processing Latency**

---

## 🗂️ Project Structure

```
crypto-trade-simulator/
│
├── app.py                         # Streamlit main app
├── models/
│   ├── impact_model.py            # Almgren-Chriss implementation
│   ├── slippage_model.py          # Regression model for slippage
│   └── fees.py                    # Maker/Taker logic
│
├── utils/
│   └── orderbook_handler.py       # WebSocket parsing and price extraction
│
│
├── requirements.txt
└── README.md
```
