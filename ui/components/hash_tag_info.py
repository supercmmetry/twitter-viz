import dash_html_components as html

from controllers import UserController


def hash_tag_info_component(controller: UserController, hash_tag: str):
    user_set = controller.hash_to_user[hash_tag]
    users_using_hashtag = len(user_set)
    total_users = len(controller.user_names)
    relevance = round(float(users_using_hashtag) / float(total_users) * 100, 2)

    return html.Div([
        html.Table([
            html.Thead(
                html.Tr([
                    html.Th("Attribute"),
                    html.Th("Value")
                ])
            ),
            html.Tbody([
                html.Tr([
                    html.Td("Hash-Tag"),
                    html.Td(hash_tag)
                ], className='bg-blue-200'),
                html.Tr([
                    html.Td("Users"),
                    html.Td(
                        str(users_using_hashtag)
                    )
                ]),
                html.Tr([
                    html.Td("Score"),
                    html.Td(str(relevance) + "%")
                ], className='bg-blue-200'),
            ])
        ],
            className='table-auto')
    ], className='flex-col border-2 rounded-md border-blue-700 m-2 p-2')
