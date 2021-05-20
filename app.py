import dash_core_components as dcc
import dash_html_components as html

import ui
from deps import app

print(dcc.__version__)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='extra-content', className='fixed'),
    html.Div(id='page-content', className='w-screen h-screen', children=[
        ui.home_page
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
