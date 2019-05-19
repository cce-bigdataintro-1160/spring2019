#!/usr/bin/env python3

import pandas as pd
import os
from plotly.offline import plot
import plotly.graph_objs as go

insurance_df = pd.read_csv('data/insurance.csv',
                           sep=',',
                           header=0)

os.makedirs('plots/16-plotly_basic', exist_ok=True)

fig = go.Figure()
fig.add_scatter(x=insurance_df['bmi'],
                y=insurance_df['charges'],
                mode='markers',
                marker={'color': insurance_df['children'],
                        'opacity': 0.6,
                        'colorscale': 'Viridis'
                        })
plot(fig, filename='./plots/plotly-scatter.html', auto_open=False)

trace = go.Heatmap(z=insurance_df.corr().round(2),
                   x=insurance_df.columns,
                   y=insurance_df.columns)

plot([trace], filename='./plots/16-plotly_basic/plotly-heatmap.html', )


