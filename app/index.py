#!/usr/bin/env python

""" Index
"""
import warnings; warnings.simplefilter('ignore', category=FutureWarning)

from importlib import import_module

from flask import redirect

from dash import html, dcc
from dash.dependencies import Input, Output

from component.layout.navbar import navbar

# /
from page.home.view import layout as home

# /movies
from page.movies.controller import *
from page.movies.view import layout as movies

# /404
from page.not_found.view import layout as not_found

from config import config
from app import app


server = app.server

def serve_content():
    url_routing = dcc.Location(id='url', refresh=False)
    app_content = html.Div(id='page-content')
    return html.Div([navbar, url_routing, app_content])

app.layout = serve_content()


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home()
    if pathname == '/movies':
        return movies()
    else:
        return not_found()


if __name__ == '__main__':
    app.run_server(
        debug=config.APP_DEBUG,
        host=config.APP_HOST,
        port=config.APP_PORT
    )
