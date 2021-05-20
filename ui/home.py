import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from controller_deps import tweet_controller, user_controller
from deps import app
from ui.components.tweet import tweet_list_component, tweet_cytoscape_component


def appbar():
    return html.Div([
        html.Button(
            html.Span('Twitter-Viz', className='text-lg font-bold text-white whitespace-nowrap'),
            className='h-11 mt-2.5 ml-2.5 p-1.5 border-0 bg-blue-700 rounded-md w-min '
                      'outline-none focus:outline-none transition-all hover:bg-blue-600',
            id='home-appbar-button'
        ),
        dcc.Input(
            id='home-query',
            className='ml-4 mt-2.5 h-11 bg-blue-700 hover:bg-blue-600 text-white border-0 rounded-md p-1 '
                      'font-bold placeholder-white transition-all',
            placeholder='Enter query',
        ),
        dcc.Input(
            id='home-query-limit',
            className='ml-4 mt-2.5 h-11 bg-blue-700 hover:bg-blue-600 text-white border-0 rounded-md p-1 '
                      'font-bold placeholder-white transition-all',
            placeholder='Enter query limit',
        )
    ],
        className='w-full h-16 bg-blue-100 select-none flex'
    )


def body():
    return html.Div([
        html.Div([], id='home-body-tweet-list'),
        html.Div([
            html.Div([], id='home-body-graphs-tweets'),
            html.Div([], id='home-body-user-info', className='mt-2'),
        ], id='home-body-graphs', className='ml-2 flex-col')
    ],
        id='home-body',
        className='ml-2 mt-2 flex'
    )


@app.callback(
    [Output('home-body-tweet-list', 'children'), Output('home-body-graphs-tweets', 'children')],
    [Input('home-appbar-button', 'n_clicks')],
    [State('home-query', 'value'), State('home-query-limit', 'value')],
    prevent_initial_call=True
)
def on_appbar_button_click(n_clicks: int, query: str, limit: str):
    tweet_controller.twint_query(query, int(limit))
    tweet_controller.load_hash_tags()

    user_controller.load_from_tweets(tweet_controller.tweets)
    user_controller.load_hash_to_user_dict()

    return tweet_list_component(tweet_controller), tweet_cytoscape_component(tweet_controller)


def page():
    return html.Div([
        appbar(),
        body()
    ])


home_page = page()
