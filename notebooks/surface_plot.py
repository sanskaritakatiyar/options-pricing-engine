import sys
sys.path.append('../src')

import numpy as np
import plotly.graph_objects as go
from bsm import bsm_price

K, T, r = 22000, 0.083, 0.065

spots = np.linspace(20000, 24000, 30)
vols = np.linspace(0.10, 0.40, 30)

S_grid, V_grid = np.meshgrid(spots, vols)

prices = np.zeros_like(S_grid)

for i in range(S_grid.shape[0]):
    for j in range(S_grid.shape[1]):
        prices[i, j] = bsm_price(S_grid[i, j], K, T, r, V_grid[i, j])

fig = go.Figure(data=[go.Surface(x=spots, y=vols, z=prices)])

fig.update_layout(
    title='Call option price surface',
    scene=dict(
        xaxis_title='Spot price',
        yaxis_title='Volatility',
        zaxis_title='Call price'
    )
)

fig.write_html('../outputs/price_surface.html')
print("Saved surface plot to outputs/price_surface.html")