import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go

import constants
from consume_streams import get_next_stream_message


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

newest_value = constants.MIN_VALUE


@app.callback(
    Output("live-graph", "figure"),
    [Input("graph-update", "n_intervals")],
)
def update_graph(n):
    value = next(get_next_stream_message())

    data = plotly.graph_objs.Bar(
        x=[value],
    )

    if value <= constants.ENERGY_NEEDED_THRESHOLD:
        status_color = "green"
    elif constants.ENERGY_NEEDED_THRESHOLD < value < constants.NEARLY_DYING_THRESHOLD:
        status_color = "yellow"
    else:
        status_color = "red"

    return {
        "data": [data],
        "layout": go.Layout(
            xaxis={"range": [constants.MIN_VALUE, constants.MAX_VALUE]},
            yaxis={"visible": False, "showticklabels": False},
            title=constants.PLOT_TITLE,
            colorway=[status_color],
        ),
    }


if __name__ == "__main__":
    app.run_server()
