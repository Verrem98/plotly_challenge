import plotly.graph_objects as go
import numpy as np

plot_bgcolor = "#fff"
quadrant_colors = [plot_bgcolor, "#2bad4e", "#85e043", "#f2a529", "#f25829"]
quadrant_text = ["", "<b>Hoge</b>", "<b>Voldoende</b>", "<b>Onvoldoende</b>", "<b>Geen</b>"]
n_quadrants = len(quadrant_colors) - 1
current_value = 1
min_value = 0
max_value = 3
hand_length = np.sqrt(2) / 3.5
hand_angle = np.pi * (1 - (max(min_value, min(max_value, current_value)) - min_value) / (max_value - min_value))
l_values = [0.5] + (np.ones(n_quadrants) / 2 / n_quadrants).tolist()

fig = go.Figure(
    data=[
        go.Pie(
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
        ),
    ],
    layout=go.Layout(
        showlegend=False,
        margin=dict(b=0, t=10, l=10, r=10),
        width=450,
        height=450,
        paper_bgcolor=plot_bgcolor,
        shapes=[
            go.layout.Shape(
                type="circle",
                x0=0.48, x1=0.52,
                y0=0.48, y1=0.52,
                fillcolor="#333",
                line_color="#333",
            ),
            go.layout.Shape(
                type="line",
                x0=0.5, x1=0.5 + hand_length * np.cos(hand_angle),
                y0=0.5, y1=0.5 + hand_length * np.sin(hand_angle),
                line=dict(color="#333", width=8)
            )
        ]
    )
)
fig.show()
