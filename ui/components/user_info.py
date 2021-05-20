import dash_html_components as html

from controllers import UserController


def user_info_component(controller: UserController, user_name: str):
    user = controller.get_by_username(user_name)

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
                    html.Td("Profile Image"),
                    html.Td(
                        html.Img(
                            src=user.profile_image_url,
                            width=128,
                            height=128
                        )
                    )
                ]),
                html.Tr([
                    html.Td("Username"),
                    html.Td(user.user_name)
                ], className='bg-blue-200'),
                html.Tr([
                    html.Td("Name"),
                    html.Td(user.name)
                ]),
                html.Tr([
                    html.Td("Url"),
                    html.Td(html.A(user.url, href=user.url))
                ], className='bg-blue-200'),
                html.Tr([
                    html.Td("Followers"),
                    html.Td(user.followers)
                ]),
                html.Tr([
                    html.Td("Following"),
                    html.Td(user.following)
                ], className='bg-blue-200'),
                html.Tr([
                    html.Td("Likes"),
                    html.Td(user.likes)
                ]),
            ])
        ],
            className='table-auto')
    ], className='flex-col border-2 rounded-md border-blue-700 m-2 p-2')
