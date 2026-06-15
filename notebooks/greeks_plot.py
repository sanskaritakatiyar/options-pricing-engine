import sys
sys.path.append('../src')

import numpy as np
import plotly.graph_objects as go
from bsm import delta

K, r, sigma = 22000, 0.065, 0.18

spots = np.linspace(20000, 24000, 50)

fig = go.Figure()

for T in [0.083, 0.25, 0.50]:
    deltas = []
    for S in spots:
        d = delta(S, K, T, r, sigma)
        deltas.append(d)
    fig.add_trace(go.Scatter(x=spots, y=deltas, mode='lines',
                              name=f'T={T} years'))

fig.update_layout(
    title='Delta vs spot price across time to expiry',
    xaxis_title='NIFTY spot price',
    yaxis_title='Delta'
)

fig.write_html('../outputs/delta_vs_spot.html')
print("Saved plot to outputs/delta_vs_spot.html")