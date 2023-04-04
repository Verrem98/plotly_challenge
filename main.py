import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# opzet voor de multi-plot
specs = [[{'type': 'pie'}, {'type': 'scatter'}], [{'type': 'scatter'}, {'type': 'scatter'}]]
titles = ["Peilmomenten", "Team", "Gilde", "Kennis"]  # , "Peilmomenten"
fig = make_subplots(rows=2, cols=2, subplot_titles=titles, specs=specs)

# plotting de gauge
plot_bgcolor = "#fff"
quadrant_colors = [plot_bgcolor, "#2bad4e", "#85e043", "#f2a529", "#f25829"]
quadrant_text = ["", "<b>Hoge</b>", "<b>Voldoende</b>", "<b>Onvoldoende</b>", "<b>Geen</b>"]
n_quadrants = len(quadrant_colors) - 1
current_value = 1
min_value = 0
max_value = 3
hand_length = np.sqrt(2) / 3
hand_angle = np.pi * (1 - (max(min_value, min(max_value, current_value)) - min_value) / (max_value - min_value))
l_values = [0.5] + (np.ones(n_quadrants) / 2 / n_quadrants).tolist()

# #layout werkt mischien ook goed?
pie_layout = go.Layout(
    showlegend=False,
    margin=dict(b=0, t=0, l=0, r=0),
    width=300,
    height=300,
    paper_bgcolor=None,
    shapes=[
        go.layout.Shape(
            type="circle", xref="x", yref="y",
            x0=0.45, x1=0.55,
            y0=0.45, y1=0.55,
            fillcolor="#333",
            line_color="#333",
        ),
        go.layout.Shape(
            type="line", xref="x", yref="y",
            x0=0.5, x1=0.5 + hand_length * np.cos(hand_angle),
            y0=0.5, y1=0.5 + hand_length * np.sin(hand_angle),
            line=dict(color="#333", width=3)
        )
    ]
)

pie_data = go.Pie(
    values=l_values,
    rotation=90,
    hole=0.75,
    labels=None,
    marker_colors=quadrant_colors,
    text=quadrant_text,
    name="Gauge",
    type="pie",
    # direction="clockwise",
    sort=False,
    showlegend=False,
    hoverinfo="none",
    textinfo="none",
    textposition="outside"
)

fig.add_trace(pie_data, 1, 1)

shape1 = go.layout.Shape(
        type="circle", xref="paper", yref="paper",
        x0=0.45, x1=0.55,
        y0=0.45, y1=0.55,
        fillcolor="#333",
        line_color="#333")

shape2 = go.layout.Shape(
    type="line", xref="paper", yref="paper",
    x0=0, x1=1,  # + hand_length * np.cos(hand_angle),
    y0=0, y1=1,  # + hand_length * np.sin(hand_angle),
    line=dict(color="#333", width=3)
)

fig.add_shape(shape1)
fig.add_shape(shape2)

# drie basis plots,
fig.add_trace(go.Scatter(x=[0,1,2,3], y=[0,1,2,3]), row=2, col=1)
fig.add_trace(go.Scatter(x=[0,1,2,3], y=[0,1,2,3]), row=1, col=2)
fig.add_trace(go.Scatter(x=[0,1,2,3], y=[0,1,2,3]), row=2, col=2)

fig.show()