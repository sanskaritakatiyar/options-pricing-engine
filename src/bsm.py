import numpy as np
from scipy.stats import norm

def bsm_price(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    if option_type == 'call':
        return round(S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2), 4)
    return round(K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1), 4)

def delta(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    if option_type == 'call':
        return round(norm.cdf(d1), 4)
    return round(norm.cdf(d1) - 1, 4)

def gamma(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    return round(norm.pdf(d1) / (S * sigma * np.sqrt(T)), 6)

def vega(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    return round(S * norm.pdf(d1) * np.sqrt(T) / 100, 4)

def theta(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    if option_type == 'call':
        t = (-(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T)) - r * K * np.exp(-r*T) * norm.cdf(d2))
    else:
        t = (-(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T)) + r * K * np.exp(-r*T) * norm.cdf(-d2))
    return round(t / 365, 4)

def rho(S, K, T, r, sigma, option_type='call'):
    d2 = ((np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))) - sigma*np.sqrt(T)
    if option_type == 'call':
        return round(K * T * np.exp(-r*T) * norm.cdf(d2) / 100, 4)
    return round(-K * T * np.exp(-r*T) * norm.cdf(-d2) / 100, 4)

if __name__ == "__main__":
    S, K, T, r, sigma = 22000, 22000, 0.083, 0.065, 0.18
    print(f"Call price : {bsm_price(S, K, T, r, sigma)}")
    print(f"Delta      : {delta(S, K, T, r, sigma)}")
    print(f"Gamma      : {gamma(S, K, T, r, sigma)}")
    print(f"Vega       : {vega(S, K, T, r, sigma)}")
    print(f"Theta      : {theta(S, K, T, r, sigma)}")
    print(f"Rho        : {rho(S, K, T, r, sigma)}")