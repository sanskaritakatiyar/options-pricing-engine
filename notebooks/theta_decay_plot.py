import sys
sys.path.append('../src')

import numpy as np
import plotly.graph_objects as go
from bsm import bsm_price

S, r, sigma = 22000, 0.065, 0.18

times = np.linspace(0.25, 0.001, 50)  # counting down from 3 months to near-zero

fig = go.Figure()

for K, label in [(20000, 'In the money (K=20000)'), 
                  (22000, 'At the money (K=22000)'), 
                  (24000, 'Out of the money (K=24000)')]:

    prices = []
    for T in times:
        p = bsm_price(S, K, T, r, sigma)
        prices.append(p)
    fig.add_trace(go.Scatter(x=times, y=prices, mode='lines', name=label))

fig.update_layout(
    title='Option price decay as expiry approaches',
    xaxis_title='Time to expiry (years)',
    yaxis_title='Call option price',
    xaxis=dict(autorange='reversed')
)

fig.write_html('../outputs/theta_decay.html')