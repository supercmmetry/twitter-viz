import dash_cytoscape as cyto
import dash_html_components as html
import networkx as nx
from dash.dependencies import Output, Input

from controller_deps import user_controller
from controllers import TweetController
from deps import app
from models import TweetModel
from ui.components.hash_tag_info import hash_tag_info_component
from ui.components.user_info import user_info_component


def tweet_component(tweet: TweetModel):
    return html.Div(
        [
            html.Span('Author: ' + tweet.user_name, className='text-white font-bold'),
            html.Br(),
            html.Span('Text: ' + tweet.text, className='text-white font-medium'),
        ],
        className='mt-2 p-2 border-0 rounded-md bg-blue-700'
    )


def tweet_list_component(controller: TweetController):
    return html.Div([
        tweet_component(obj)
        for obj in controller.tweets
    ],
        className='w-4/12 overflow-y-auto border-2 rounded-md p-2 border-blue-700',
        style={
            'height': 'calc(100vh - 6rem)'
        }
    )


def tweet_cytoscape_component(controller: TweetController):
    graph = nx.Graph()
    cyto_nodes = []
    cyto_edges = []

    for tweet in controller.tweets:
        graph.add_node(tweet.user_name)
        cyto_nodes.append({
            'data': {
                'id': tweet.user_name,
                'label': tweet.user_name,
                'type': 'user'
            },
            'classes': 'user',
        })

    for hash_tag in controller.hash_tags:
        graph.add_node(hash_tag)
        cyto_nodes.append({
            'data': {
                'id': hash_tag,
                'label': hash_tag,
                'type': 'hashtag'
            },
            'classes': 'hashtag',
        })

    for tweet in controller.tweets:
        for hash_tag in list(set(tweet.hash_tags)):
            graph.add_edge(tweet.user_name, hash_tag)
            cyto_edges.append({
                'data': {
                    'source': tweet.user_name,
                    'target': hash_tag
                },

            })

    pos_layout = nx.random_layout(graph)

    index = 0
    for node in graph.nodes():
        x, y = pos_layout[node]
        x *= 800
        y *= 500
        cyto_nodes[index]['position'] = {'x': x, 'y': y}
        index += 1

    cytoscape = cyto.Cytoscape(
        id='home-body-graphs-tweets-cytoscape',
        layout={'name': 'preset'},
        style={'width': '60vw', 'height': '40vh'},
        elements=cyto_nodes + cyto_edges,
        stylesheet=[
            {
                'selector': 'node',
                'style': {
                    'content': 'data(label)'
                }
            },
            {
                'selector': 'edge',
                'style': {
                    'curve-style': 'bezier',
                    'line-color': 'green',
                    'target-arrow-shape': 'vee',
                    'target-arrow-color': 'green',
                    'mid-target-arrow-color': 'green',
                    'mid-target-arrow-shape': 'circle',
                }
            },
            {
                'selector': '.user',
                'style': {
                    'background-color': '#eb15e0',
                }
            },
            {
                'selector': '.hashtag',
                'style': {
                    'background-color': '#21d1c5',
                }
            }
        ]
    )

    return html.Div([
        html.Span('User-HashTag two-mode network',
                  className='mt-1 mb-2 text-md font-bold text-white border-0 rounded-md bg-blue-700 p-2'),
        cytoscape
    ], className='p-2 mt-1 mr-1 border-2 rounded-md border-blue-700')


@app.callback(
    [Output('home-body-user-info', 'children')],
    [Input('home-body-graphs-tweets-cytoscape', 'tapNodeData')],
    prevent_initial_call=True
)
def on_user_node_click(data):
    if data is None:
        return ['']
    if data['type'] == 'user':
        return [user_info_component(user_controller, data['id'])]
    else:
        return [hash_tag_info_component(user_controller, data['id'])]
