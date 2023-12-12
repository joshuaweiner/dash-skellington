#!/usr/bin/env python

""" Page View
"""

import dash
from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc

import pandas as pd

from config import config


credit = pd.read_csv(config.APP_DATA_DIR / 'references.csv').assign(
    name=lambda df: df.apply(lambda x: f"[{x['name']}]({x['url']})", axis=1)
)

content = html.Div(
    dbc.Container(
        [
           dbc.Container(
                [
                    html.H1('Welcome to Dash-Skeleton', className='display-3'),
                    html.P(
                        'Dash-Skeleton is a "skeleton" Plotly Dash project that puts forth a '
                        'set of conventions, project structure, and best practices. This project '
                        'was inspired by many people please refer to the credits section for more information.',
                        className='lead'
                    ),
                    html.P(
                        [
                            'The data used to fuel this project is from ',
                            html.A('Rounak Banik.', href='https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset')
                        ]
                    ),
                    html.Hr(className='my-2'),
                    html.P(
                        dbc.Button(
                            "Visit Dashboard",
                            href='/movies',
                            color="primary"),
                        className='lead py-3'
                    ),
                    html.Div(
                        dash_table.DataTable(
                                id='credit-table',
                                columns=[
                                    {"name": 'Type', "id": 'type', 'type': 'text'},
                                    {"name": 'Name', "id": 'name', 'presentation': 'markdown'},
                                ],
                                data=credit.to_dict('records'),
                                markdown_options={"html": True},
                                style_cell={
                                    'backgroundColor': '#ECF0F1',
                                    'color': '#2C3E50',
                                    'borderColor': '#2C3E50',
                                },
                                style_header={
                                    'backgroundColor': '#2C3E50',
                                    'color': '#ECF0F1',
                                    'borderColor': '#2C3E50',
                                },
                                style_cell_conditional=[
                                    {'if': {'column_id': 'type'}, 'textAlign': 'center', 'width': '50%'},
                                    {'if': {'column_id': 'name'}, 'textAlign': 'center', 'width': '50%'},
                                ],
                        ), className='pb-3'
                    )
                ], fluid=True
            ),
        ], fluid=False,  className="gap-3 p-3 bg-light rounded-3",
    ),
)

def layout():
    return content
