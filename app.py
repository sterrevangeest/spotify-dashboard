import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from datetime import datetime as dt
from dateutil.parser import parse

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

df = pd.read_csv("data/data_complete-kopie.csv")
df['Date'] = df['Date'].astype('datetime64[ns]')
df = df.copy()
df_average = df.groupby("Date")["Valence"].mean()
df_average = df_average.reset_index()
df_average["Week"] = df_average["Date"].dt.strftime("%V")
df_average["Year"] = df_average['Date'].dt.year

fig = px.line(df_average, x="Week", y="Valence", color="Year")

# fig.update_layout(
#     plot_bgcolor='#0d2137',
#     paper_bgcolor='#0d2137',
#     font_color="#fff"
# )

app.layout = html.Div(children=[
    html.H1(children='Spotify Mood Dashboard', className="app-header--title"),

    html.P(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
