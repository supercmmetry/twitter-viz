import dash_html_components as html


def div(child, class_name=''):
    return html.Div([
        child
    ], className=class_name)
