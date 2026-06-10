import numpy as np
from scipy.stats import norm

def bsm_price(S, K, T, r, sigma, option_type='call'):
    """
    Black-Scholes-Merton option pricing formula.
    
    S     : current stock price
    K     : strike price
    T     : time to expiry in years (e.g. 0.5 = 6 months)
    r     : risk-free rate as decimal (e.g. 0.065 for 6.5%)
    sigma : volatility as decimal (e.g. 0.20 for 20%)
    """
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    if option_type == 'call':
        price = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    elif option_type == 'put':
        price = K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")
    
    return round(price, 4)


if __name__ == "__main__":
    # Quick test: NIFTY-like call option
    price = bsm_price(S=22000, K=22000, T=0.083, r=0.065, sigma=0.18)
    print(f"Call option price: {price}")