import numpy as np
import plotly.graph_objects as go

def animate_gss(f, history, const_a, const_b, title="Golden Section Search Animation"):
    margin = (const_b - const_a) * 0.2
    x_vals = np.linspace(const_a - margin, const_b + margin, 500)
    y_vals = f(x_vals)

    frames = []
    for i, (a, b, x1, x2, f1, f2) in enumerate(history):
        frames.append(go.Frame(
            data=[
                go.Scatter(x=x_vals, y=y_vals, mode='lines', name='f(x)'),
                go.Scatter(x=[x1, x2], y=[f1, f2], mode='markers+text',
                           text=[f"x1={x1:.2f}", f"x2={x2:.2f}"], textposition="top center",
                           marker=dict(size=8, color='red'), name='Candidates'),
                go.Scatter(x=[a, b], y=[f(a), f(b)], mode='markers',
                           marker=dict(size=8, color='green'), name='Interval')
            ],
            name=str(i)
        ))

    fig = go.Figure(
        data=[
            go.Scatter(x=x_vals, y=y_vals, mode='lines', name='f(x)'),
            go.Scatter(x=[], y=[], mode='markers+text', name='Candidates'),
            go.Scatter(x=[], y=[], mode='markers', name='Interval')
        ],
        layout=go.Layout(
            title=title,
            xaxis_title="x",
            yaxis_title="f(x)",
            updatemenus=[{
                "type": "buttons",
                "buttons": [{
                    "label": "Play",
                    "method": "animate",
                    "args": [None, {
                        "frame": {"duration": 600, "redraw": True},
                        "fromcurrent": True
                    }]
                }]
            }]
        ),
        frames=frames
    )

    return fig
