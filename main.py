import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import math

# opzet voor de multi-plot
specs = [[{'type': 'domain'}, {'type': 'scatter'}], [{'type': 'scatter'}, {'type': 'scatter'}]]
titles = ["Peilmomenten", "Team", "Gilde", "Kennis"]  # , "Peilmomenten"
fig = make_subplots(rows=2, cols=2, subplot_titles=titles, specs=specs)

# plotting de gauge
plot_bgcolor = "#fff"
quadrant_colors = ["#2bad4e", "#85e043", "#f2a529", "#f25829"]
quadrant_text = ["", "<b>Hoge</b>", "<b>Voldoende</b>", "<b>Onvoldoende</b>", "<b>Geen</b>"]

n_quadrants = len(quadrant_colors)
total_reference_moments = 24
current_reference_moment = 15

# deel de gauge op in n quadrants (met getallen die niet heel deelbaar zijn door n is het laatste quadrant nu korter)
gauge_quadrants = list(
    range(0, math.ceil(total_reference_moments + total_reference_moments / n_quadrants),
          math.ceil(total_reference_moments / n_quadrants)))

gauge = go.Indicator(
    mode="gauge+delta",
    value=current_reference_moment,
    delta={'reference': 0, 'increasing': {
        'color': quadrant_colors[[current_reference_moment > x for x in gauge_quadrants].index(False) - 1],
        'symbol': ''}},
    gauge={
        'axis': {'range': [None, total_reference_moments], 'dtick': math.ceil(total_reference_moments / n_quadrants)},
        'bar': {'color': "black", 'thickness': 0.1},
        'bgcolor': plot_bgcolor,
        'steps': [
            {'line': {'width': 0}, 'range': [gauge_quadrants[i], gauge_quadrants[i + 1]], 'color': quadrant_colors[i]}
            for i in
            range(len(gauge_quadrants) - 1)],
        'threshold': {
            'line': {'color': "black", 'width': 6},
            'thickness': 0.4,
            'value': current_reference_moment}})

fig.add_trace(gauge, 1, 1)

shape1 = go.layout.Shape(
    type="circle", xref="paper", yref="paper",
    x0=0.45, x1=0.55,
    y0=0.45, y1=0.55,
    fillcolor="#333",
    line_color="#333")

fig.add_shape(shape1)

# drie basis plots,
fig.add_trace(go.Scatter(x=[0, 1, 2, 3], y=[0, 1, 2, 3]), row=2, col=1)
fig.add_trace(go.Scatter(x=[0, 1, 2, 3], y=[0, 1, 2, 3]), row=1, col=2)
fig.add_trace(go.Scatter(x=[0, 1, 2, 3], y=[0, 1, 2, 3]), row=2, col=2)

# zet de titels iets naar boven zodat ze niet clippen met de tekst van de gauge
for annotation in fig['layout']['annotations']:
    annotation['height'] = 70

fig.show()
