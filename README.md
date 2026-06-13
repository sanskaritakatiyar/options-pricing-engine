# Options Pricing Engine

A Black-Scholes-Merton options pricing engine built from scratch in Python, with Greeks, implied volatility, and interactive visualizations.

## What it does
- Prices European call and put options using the BSM formula
- Computes all 5 Greeks: Delta, Gamma, Vega, Theta, Rho
- Solves for implied volatility using Newton-Raphson, with convergence checks and stability safeguards
- Visualizes option price sensitivity with interactive 2D and 3D charts
- Validated against NIFTY 50 at-the-money options

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

## Tech stack
Python · NumPy · SciPy · Plotly

## Project structure
options-pricing-engine/

├── src/

│   └── bsm.py              # pricing, Greeks, implied vol

├── notebooks/

│   ├── price_plot.py       # 2D comparison chart

│   └── surface_plot.py     # 3D surface chart

├── outputs/                 # generated charts

└── README.md

## How to run
pip install numpy scipy plotly
python src/bsm.py
python notebooks/price_plot.py
python notebooks/surface_plot.py

## Next steps
- Live NIFTY option chain comparison using yfinance
- Greeks surface plots (delta, gamma, vega vs spot and time)
