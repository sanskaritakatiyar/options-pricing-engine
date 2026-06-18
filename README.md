# Options Pricing Engine

A Black-Scholes-Merton options pricing engine built from scratch in Python, with Greeks, implied volatility, live market validation, and interactive visualizations.

## What it does
- Prices European call and put options using the BSM formula
- Computes all 5 Greeks: Delta, Gamma, Vega, Theta, Rho
- Solves for implied volatility using Newton-Raphson, with convergence checks and stability safeguards for low-vega edge cases (deep ITM/OTM, very short expiry)
- Validates model output against live AAPL option chain data — model prices match market prices to within rounding error
- Visualizes option price sensitivity with interactive 2D and 3D charts

## Sample output
Call price : 515.5026
Delta      : 0.5517
Gamma      : 0.000347
Vega       : 25.0729
Theta      : -9.5183
Rho        : 9.6462
Implied vol: 0.2137

## Visualizations
- `outputs/price_vs_spot.html` — call price vs spot price across volatility levels
- `outputs/price_surface.html` — 3D surface of call price across spot price and volatility
- `outputs/delta_vs_spot.html` — delta vs spot price across different times to expiry
- `outputs/theta_decay.html` — option price decay as expiry approaches, across moneyness

## Live data validation
Used `implied_vol()` to back out volatility from real AAPL option chain prices, then fed that volatility back into `bsm_price()` to confirm it reproduces the original market price. Confirmed near-exact matches for near-the-money strikes. Found and documented that the solver becomes unstable for deep ITM/OTM options and very short-dated options — both cases where vega (and therefore the Newton-Raphson step size) becomes too small to converge reliably. Fixed by filtering to strikes within 5% of spot price.

## Tech stack
Python · NumPy · SciPy · Plotly · yfinance

## Project structure
options-pricing-engine/

├── src/

│   └── bsm.py                   # pricing, Greeks, implied vol

├── notebooks/

│   ├── price_plot.py            # 2D price vs spot chart

│   ├── surface_plot.py          # 3D price surface

│   ├── greeks_plot.py           # delta vs spot across expiries

│   ├── theta_decay_plot.py      # time decay chart

│   ├── explore_data.py          # yfinance data exploration

│   └── live_comparison.py       # live market validation

├── outputs/                     # generated charts

└── README.md

## How to run
pip install -r requirements.txt
python src/bsm.py
python notebooks/price_plot.py
python notebooks/surface_plot.py
python notebooks/greeks_plot.py
python notebooks/theta_decay_plot.py
python notebooks/live_comparison.py

## Next steps
- Volatility smile plot across strikes using real option chain data
- Gamma surface visualization