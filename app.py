import dash
import dash_core_components as dcc
import dash_html_components as html
from deps import app
import ui

print(dcc.__version__)

app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),

    # content will be rendered in this element
    html.Div(id='page-content', className='w-screen h-screen', children=[
        ui.home_page
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)
