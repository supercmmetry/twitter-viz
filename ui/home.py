import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from deps import app


def appbar():
    return html.Div([
        html.Button(
            html.Span('Twitter-Viz', className='text-lg font-bold text-white whitespace-nowrap'),
            className='float-left mt-2.5 ml-2.5 p-1.5 border-0 bg-blue-700 rounded-md w-min '
                      'outline-none focus:outline-none transition-all hover:bg-blue-600',
            id='appbar-button'
        )
    ], className='w-full h-16 bg-blue-100 select-none')


@app.callback(
    [Output('appbar-button', 'value')],
    [Input('appbar-button', 'n_clicks')]
)
def on_appbar_button_click(n_clicks: int):
    if n_clicks is not None and n_clicks > 0:
        print('appbar button clicked!')
    return [None]


def page():
    return html.Div([
        appbar()
    ])


home_page = page()
