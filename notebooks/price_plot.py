import sys
sys.path.append('../src')

import numpy as np
import plotly.graph_objects as go
from bsm import bsm_price

K, T, r = 22000, 0.083, 0.065

spots = np.linspace(20000, 24000, 50)

fig = go.Figure()

for sigma in [0.10, 0.18, 0.30]:
    prices = []
    for S in spots:
        p = bsm_price(S, K, T, r, sigma)
        prices.append(p)
    fig.add_trace(go.Scatter(x=spots, y=prices, mode='lines', 
                              name=f'sigma={sigma}'))

fig.update_layout(
    title='Call option price vs spot price',
    xaxis_title='NIFTY spot price',
    yaxis_title='Call option price'
)

fig.write_html('../outputs/price_vs_spot.html')
print("Saved plot to outputs/price_vs_spot.html")