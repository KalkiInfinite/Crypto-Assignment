def estimate_slippage(orderbook, amount_usd):
    asks = orderbook["asks"]
    total_cost = 0
    qty_accum = 0
    for price, qty in asks:
        price = float(price)
        qty = float(qty)
        trade_val = price * qty
        if total_cost + trade_val >= amount_usd:
            needed_qty = (amount_usd - total_cost) / price
            qty_accum += needed_qty
            total_cost += needed_qty * price
            break
        else:
            total_cost += trade_val
            qty_accum += qty

    avg_price = total_cost / qty_accum
    best_bid = float(orderbook['bids'][0][0])
    best_ask = float(orderbook['asks'][0][0])
    mid_price = (best_bid + best_ask) / 2
    slippage = avg_price - mid_price
    return round(slippage, 2), round(avg_price, 2)

def estimate_fees(amount_usd, fee_rate=0.001):
    return round(amount_usd * fee_rate, 2)

def estimate_market_impact(volatility, amount_usd, liquidity=1_000_000):
    impact = (volatility * amount_usd) / liquidity
    return round(impact, 4)
