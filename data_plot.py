#!/usr/bin/env python

import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Bar(
    x=[2004.5, 2007.5, 2012, 2015, 2018],
    y=[3.5, 2.6, 5.0, 1000.0, 10000.0],
    width = [1, 5, 3, 3, 2]
)

data = [trace0]

fig = go.Figure(data=data)
py.iplot(fig, filename='width-bar')
