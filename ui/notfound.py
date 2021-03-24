import dash
import dash_core_components as dcc
import dash_html_components as html


def page():
    return html.Div([
        html.H1('404'),
        html.H2('Page Not Found'),
    ])


not_found_page = page()
