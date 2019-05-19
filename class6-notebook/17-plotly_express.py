#!/usr/bin/env python3

import pandas as pd
import os
from plotly.offline import plot
import plotly.graph_objs as go


insurance_df = pd.read_csv('data/insurance.csv',
                           sep=',',
                           header=0)

os.makedirs('plots/16-plotly_basic', exist_ok=True)


# plot([trace], filename='./plots/16-plotly_basic/plotly-heatmap.html', )


