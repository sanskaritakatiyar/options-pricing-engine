import sys
sys.path.append('../src')

import yfinance as yf
from datetime import datetime
from bsm import bsm_price, implied_vol

ticker = yf.Ticker("AAPL")
S = ticker.history(period='1d')['Close'].iloc[-1]

expiry = "2026-06-19"
chain = ticker.option_chain(expiry)
calls = chain.calls

today = datetime.now()
expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
T = (expiry_date - today).days / 365

r = 0.045  # approx US risk-free rate

print(f"AAPL spot price: {S:.2f}")
print(f"Time to expiry: {T:.4f} years\n")

print(f"{'Strike':>8} {'Market Price':>14} {'Implied Vol':>12} {'Model Price':>12}")

for _, row in calls.head(10).iterrows():
    K = row['strike']
    market_price = row['lastPrice']
    
    if market_price <= 0:
        continue
    
    iv = implied_vol(market_price, S, K, T, r)
    model_price = bsm_price(S, K, T, r, iv)
    
    print(f"{K:>8.2f} {market_price:>14.2f} {iv:>12.4f} {model_price:>12.2f}")