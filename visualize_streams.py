import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go

from consume_streams import get_next_stream_message


# VORN data
from mode.utils.text import title

MIN_VALUE = 80.0
MAX_VALUE = 200.0

ENERGY_NEEDED_THRESHOLD = 140.0
NEARLY_DYING_THRESHOLD = 185.0


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(id="live-graph", animate=True),
        dcc.Interval(
            id="graph-update",
            interval=1000,
            n_intervals=0,
        ),
    ]
)


@app.callback(
    Output("live-graph", "figure"),
    [Input("graph-update", "n_intervals")],
)
def update_graph(n):
    value = next(get_next_stream_message())

    data = plotly.graph_objs.Bar(
        x=[value],
    )

    if value <= ENERGY_NEEDED_THRESHOLD:
        status_color = "green"
    elif ENERGY_NEEDED_THRESHOLD < value < NEARLY_DYING_THRESHOLD:
        status_color = "yellow"
    else:
        status_color = "red"

    return {
        "data": [data],
        "layout": go.Layout(
            xaxis={"range": [MIN_VALUE, MAX_VALUE]},
            yaxis={"visible": False, "showticklabels": False},
            title="Cross-Country Battery",
            colorway=[status_color],
        ),
    }


if __name__ == "__main__":
    app.run_server()
