import data
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from datetime import datetime as dt

app = dash.Dash(__name__)

df = data.get_data()

df_average = df.copy()
df_average = df_average.groupby("Date")["Valence"].mean()
df_average = df_average.reset_index()

# assign dates again
df_average["Week"] = df_average["Date"].dt.strftime("%V")
df_average['Day'] = df_average["Date"].dt.strftime("%m-%d")
df_average['Month'] = pd.to_datetime(
    df_average['Date'], format='%m').dt.month_name()
df_average["Year"] = df_average['Date'].dt.year

df_2019 = df_average[df_average["Year"] == 2019]
df_2020 = df_average[df_average["Year"] == 2020]

# max week 42 in 2019
mask_2019 = (df_average['Date'] >= '2019-01-04') & (
    df_average['Date'] <= '2019-10-18')

df_2019 = df_average.loc[mask_2019]

df_complete = pd.concat([df_2019, df_2020])

fig = px.line(df_complete, x="Week", y="Valence",
              hover_data={"Month", "Day"},
              color="Year", line_shape='spline')


app.layout = html.Div(children=[
    html.H1(children='Does COVID-19 influence our listening mood?',
            className="app-header--title"),
    html.P(children='This dashboard shows our listening mood based on weekly published top 200-most-streamed songs. The mood of a song is classified by its valence value: a measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry.)',
           className=""),


    html.H3(children='Average valance for both years'),

    dcc.Graph(
        figure=fig
    )
], className="lines")

fig.update_layout(
    plot_bgcolor='#0d2137',
    paper_bgcolor='#0d2137',
    font_color="#fff",
    colorway=["#0d2137", "#fff"],
    xaxis=dict(
        tickmode='linear',
        tick0=0,
        dtick=10
    ),
    yaxis=dict(
        tickmode='linear',
        tick0=0,
        dtick=0.02
    )
)


def get_html_element():
    return app.layout
