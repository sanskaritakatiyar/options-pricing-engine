import yfinance as yf

ticker = yf.Ticker("AAPL")
print("Current price:", ticker.history(period='1d')['Close'].iloc[-1])

expirations = ticker.options
print("Available expiry dates:", expirations[:5])  # just show first 5