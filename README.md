# Options Pricing Engine

A Black-Scholes-Merton options pricing engine built from scratch in Python.

## What it does
- Prices European call and put options using the BSM formula
- Computes all 5 Greeks: Delta, Gamma, Vega, Theta, Rho
- Validated against NIFTY 50 at-the-money options

## Sample output
Call price : 515.5026
Delta      : 0.5517
Gamma      : 0.000347
Vega       : 25.0729
Theta      : -9.5183
Rho        : 9.6462

## Tech stack
Python · NumPy · SciPy

## How to run
pip install numpy scipy
python src/bsm.py

## Next steps
- Implied volatility solver (Newton-Raphson)
- Interactive 3D surface plots (Plotly)
- Live NIFTY option chain comparison# options-pricing-engine
