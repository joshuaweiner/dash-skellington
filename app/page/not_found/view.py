#!/usr/bin/env python

""" Page View
"""

from dash import html, dcc
import dash_bootstrap_components as dbc


def layout():
    return html.Div(children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3('404: Page Not Found'),
                    ],
                    align='center',
                    class_name='text-center'
                )
            ],
            align='center'
        )
    ], className='py-2'
)
