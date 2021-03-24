import ui


def route(pathname: str):
    _route_map = {
        "home": ui.home_page
    }

    if pathname not in _route_map:
        return ui.not_found_page
    else:
        return _route_map[pathname]
