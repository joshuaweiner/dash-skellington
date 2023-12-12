#!/usr/bin/env python

"""
Generates styled DataTable from a  DataFrame, formatted with custom column alignments and pagination.
"""

import dash


def create_movie_table(df):
    return dash.dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df.columns],
        page_size=20,
        style_header={
            'fontWeight': 'bold',
            'fontFamily': 'Open-Sans, sans-serif'
        },
        style_cell={
            'fontFamily': 'Open-Sans, sans-serif'  
        },
        style_cell_conditional=[
            {'if': {'column_id': 'name'}, 'textAlign': 'left'},
            {'if': {'column_id': 'rating'}, 'textAlign': 'center'},
            {'if': {'column_id': 'genre'}, 'textAlign': 'center'},
            {'if': {'column_id': 'year'}, 'textAlign': 'center'},
            {'if': {'column_id': 'budget'}, 'textAlign': 'right'},
            {'if': {'column_id': 'score'}, 'textAlign': 'center'},
            {'if': {'column_id': 'country'}, 'textAlign': 'center'}
        ],
    )
