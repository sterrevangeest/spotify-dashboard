import data
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
from datetime import datetime as dt
from dateutil.parser import parse

app = dash.Dash(__name__)

df = data.get_data()

df_unique = df.drop_duplicates(subset=["Song"])
df_2019 = df_unique[df_unique["Year"] == 2019]
df_2020 = df_unique[df_unique["Year"] == 2020]

df_complete = pd.concat([df_2019, df_2020])

fig = px.histogram(df_complete, x="Valence",
                   color="Year", nbins=20)

app.layout = html.Div(children=[
    html.H3(children='Distribution of tracks streamed, by valence'),

    dcc.Graph(
        id='example-graph',
        figure=fig,

    )
], className="histogram")

fig.update_layout(
    plot_bgcolor='#0d2137',
    paper_bgcolor='#0d2137',
    font_color="#fff",
    colorway=["#0d2137", "#fff"]
)


def get_html_element():
    return app.layout
