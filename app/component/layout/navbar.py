#!/usr/bin/env python

""" Navbar
"""
from dash import Input, Output, State, html
import dash_bootstrap_components as dbc

from config import config
from app import app


LOGO = app.get_asset_url('logo.png')

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand(config.APP_TITLE, className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            html.A('Dashboard', href='/movies'),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
        ],
        fluid=True
    ),
    color='light',
    dark=False,
    class_name='mb-4'
)


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
