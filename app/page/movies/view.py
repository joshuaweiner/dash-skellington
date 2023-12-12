from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_daq as daq


content = html.Div(
    [
        dcc.Store(id='data-store'),
        dcc.Interval(id='placeholder-id', interval=1*1000, n_intervals=0, max_intervals=1),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.CardGroup(
                                [
                                    dbc.Card(
                                        [
                                            html.H5('Movies', className='card-title'),
                                            html.H1(id='stat-number-movie', className='card-text')
                                        ],
                                        className='mb-4', color='dark', inverse=True,
                                        style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'}
                                    ),
                                    dbc.Card(
                                        [
                                            html.H5('Genre', className='card-title'),
                                            html.H1(id='stat-number-genre', className='card-text')
                                        ],
                                        className='mb-4', color='dark', inverse=True,
                                        style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'}
                                    ),
                                    dbc.Card(
                                        [
                                            html.H5('Country', className='card-title'),
                                            html.H1(id='stat-number-country', className='card-text')
                                        ],
                                        className='mb-4', color='dark', inverse=True,
                                        style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'}
                                    ),
                                ],
                                className='g-2 card-group',
                                style={'width': '100%'}
                            ),
                            width=12, lg=6,
                            style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'}
                        ),
                        dbc.Col(
                            dbc.Card(
                                dbc.Stack(
                                    [
                                        html.Div(
                                            [
                                                html.H6('Select Genre'), dcc.Dropdown(
                                                    id='select-genre', value=None, multi=True
                                                )
                                            ], 
                                        ),
                                        html.Div(
                                            [
                                                html.H6('Select Rating'), dcc.Dropdown(
                                                    id='select-rating', value=None, multi=True
                                                )
                                            ], 
                                        ),
                                    ],
                                    gap=3
                                ),
                                body=True,
                                style={'display': 'flex', 'justifyContent': 'center'}
                            ),
                            width=12, lg=6
                        )
                    ],
                    className='g-4 mb-4'
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        [
                                            dbc.Row(
                                                [
                                                    dbc.Col(html.P('Top/Bottom 20 Movies By Score', className='lead text-start'), align='center'),
                                                    dbc.Col(
                                                        daq.BooleanSwitch(id='toggle-table-movie', label='Switch: Top 20 / Bottom 20', on=False, style={'alignSelf': 'center'}),
                                                        style={'display': 'flex', 'justifyContent': 'end'}
                                                    )
                                                ], align='center', justify='between',
                                            )
                                        ]
                                    ),
                                    dbc.CardBody(html.Div(id='table-movie', style={'overflowX': 'auto'}))
                                ],
                                style={'height': '100%', 'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'center'}
                            ),
                            width=12, lg=6
                        ),
                        dbc.Col(
                            dbc.Card(dcc.Graph(id='plot-genre-distribution'), style={'height': '100%', 'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'center'}),
                            width=12, lg=6
                        ),
                    ],
                    className='g-4 mb-4'
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(dcc.Graph(id='plot-budget-score-scatter'), style={'height': '100%'}),
                            width=12, lg=6
                        ),
                        dbc.Col(
                            dbc.Card(dcc.Graph(id='plot-time-score-scatter'), style={'height': '100%'}),
                            width=12, lg=6,
                        ),
                    ],
                    className='g-4 mb-4'
                ),
            ],
            fluid=True
        )
    ]
)

def layout():
    return content
