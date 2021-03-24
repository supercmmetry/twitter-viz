import os
import dash

dir_path = os.path.dirname(os.path.realpath(__file__))

external_stylesheets = []
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

