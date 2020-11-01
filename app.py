import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go

import data

import lines
import histogram
import year_info

app = dash.Dash(__name__)

# import all html dash html elements from modules
year_info_element = year_info.get_html_element()
histogram_element = histogram.get_html_element()
lines_element = lines.get_html_element()

# display the elements
app.layout = html.Div(
    children=[lines_element, year_info_element, histogram_element])


if __name__ == '__main__':
    app.run_server(debug=True)
