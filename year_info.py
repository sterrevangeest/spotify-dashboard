import dash
import dash_core_components as dcc
import dash_html_components as html

import data

df = data.get_data()

app = dash.Dash(__name__)

# Split years
df_2019 = df[df["Year"] == 2019]
df_2020 = df[df["Year"] == 2020]

df_average_2019 = df_2019.groupby("Year")["Valence"].mean().round(3)
df_average_2020 = df_2020.groupby("Year")["Valence"].mean().round(3)
saddest_song_2019 = df_2019[df_2019['Valence'] == df_2019['Valence'].min()]
saddest_song_2020 = df_2020[df_2020['Valence'] == df_2020['Valence'].min()]
happiest_song_2019 = df_2019[df_2019['Valence'] == df_2019['Valence'].max()]
happiest_song_2020 = df_2020[df_2020['Valence'] == df_2020['Valence'].max()]


app.layout = html.Div(children=[
    html.Div(children=[
        html.Div(children=[
            html.H2(children='2019'),
             html.H3(children="Average valence"),
             html.P(children=df_average_2019),
             html.H3(children="Saddest song"),
             html.Div(children=[

                 html.A(href=happiest_song_2019["Url"].iloc[0],
                        children=saddest_song_2019["Song"]),
                 html.P(children=saddest_song_2019["Artist"]),
                 html.Div(children=[
                     html.P(children="Valence",
                            className="display-inline valence"),
                     html.P(
                         children=saddest_song_2019["Valence"], className="display-inline")
                 ]),
             ], className="info"),
             html.H3(children="Happiest song"),
             html.Div(children=[
                 html.A(href=happiest_song_2019["Url"].iloc[0],
                        children=happiest_song_2019["Song"]),
                 html.P(children=happiest_song_2019["Artist"]),
                 html.Div(children=[
                     html.P(children="Valence",
                            className="display-inline valence"),
                     html.P(
                         children=happiest_song_2019["Valence"], className="display-inline")
                 ]),
             ], className="info"),

             ], className="year-info"),
        html.Div(children=[
            html.H2(children='2020'),
            html.H3(children="Average valence"),
            html.P(children=df_average_2020),
            html.H3(children="Saddest song"),
            html.Div(children=[

                 html.A(href=happiest_song_2020["Url"].iloc[0],
                        children=saddest_song_2020["Song"].iloc[0]),
                 html.P(children=saddest_song_2020["Artist"].iloc[0]),
                 html.Div(children=[
                     html.P(children="Valence",
                            className="display-inline valence"),
                     html.P(
                         children=saddest_song_2020["Valence"].iloc[0], className="display-inline")
                 ]),
                 ], className="info"),
            html.H3(children="Happiest song"),
            html.Div(children=[
                html.A(href=happiest_song_2020["Url"].iloc[0],
                       children=happiest_song_2020["Song"]),
                html.P(children=happiest_song_2020["Artist"]),
                html.Div(children=[
                     html.P(children="Valence",
                            className="display-inline valence"),
                     html.P(
                         children=happiest_song_2020["Valence"], className="display-inline")
                     ]),
            ], className="info"),
        ], className="year-info"),
    ], className="years-info"),
], className="year_info")


def get_html_element():
    return app.layout
