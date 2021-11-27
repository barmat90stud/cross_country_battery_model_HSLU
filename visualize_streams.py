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
    data = plotly.graph_objs.Bar(
        x=[next(get_next_stream_message())],
    )

    return {
        "data": [data],
        "layout": go.Layout(
            xaxis={"range": [MIN_VALUE, MAX_VALUE]},
            yaxis={"visible": False, "showticklabels": False},
            title="Cross-Country Battery",
        ),
    }


if __name__ == "__main__":
    app.run_server()
