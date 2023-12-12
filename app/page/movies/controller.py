#!/usr/bin/env python

""" Page Controller
"""
import json

from dash import dash, callback_context
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np

from page.movies.model import load_model_data
from lib.utils import read_dataframe_from_store, read_list_from_store

from component.plot.create_genre_distribution import create_genre_distribution
from component.plot.create_time_score_scatter import create_time_score_scatter
from component.plot.create_budget_score_scatter import create_budget_score_scatter
from component.plot.create_movie_table import create_movie_table

from app import app


@app.callback(
    Output('data-store', 'data'),
    [Input('placeholder-id', 'n_intervals'),
     Input('select-genre', 'value'),
     Input('select-rating', 'value')],
)
def update_data_store(n_intervals, selected_genre, selected_rating):
    ctx = callback_context

    movies = load_model_data()
    genres = movies['genre'].unique()
    ratings = movies['rating'].unique()

    if not ctx.triggered:
        return json.dumps({
            'movies': movies.to_json(),
            'genres': genres.tolist(),
            'ratings': ratings.tolist()
        })
    else:
        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if trigger_id == 'placeholder-id':
            # placeholder-id triggers the callback
            genres = movies['genre'].unique()
            ratings = movies['rating'].unique()

            return json.dumps({
                'movies': movies.to_json(),
                'genres': genres.tolist(),
                'ratings': ratings.tolist()
            })
        else:
            if selected_genre:
                selected_genre = [selected_genre] if not isinstance(selected_genre, list) else selected_genre
                movies = movies[movies['genre'].isin(selected_genre)]
            if selected_rating:
                selected_rating = [selected_rating] if not isinstance(selected_rating, list) else selected_rating
                movies = movies[movies['rating'].isin(selected_rating)]

            return json.dumps({
                'movies': movies.to_json(),
                'genres': genres.tolist(),
                'ratings': ratings.tolist()
            })

@app.callback(Output('select-genre', 'options'), Input('data-store', 'data'))
def update_select_genre(data):
    genres = read_list_from_store(data, 'genres')
    options = [{'label':g, 'value':g} for g in genres if str(g) != 'nan']
    return options

@app.callback(Output('select-rating', 'options'), Input('data-store', 'data'))
def update_select_rating(data):
    ratings = read_list_from_store(data, 'ratings')
    options = [{'label':r, 'value':r} for r in ratings if str(r) != 'nan']
    return options

@app.callback([Output('stat-number-movie', 'children'),
               Output('stat-number-genre', 'children'),
               Output('stat-number-country', 'children'),
               ], Input('data-store', 'data'))
def update_data_store_statistics(data):
    movies = read_dataframe_from_store(data, 'movies')
    nmovies = len(pd.unique(movies['name']))
    ngenre = len(pd.unique(movies['genre']))
    ncountry = len(pd.unique(movies['country']))
    return nmovies, ngenre, ncountry

@app.callback(Output('plot-time-score-scatter', 'figure'), Input('data-store', 'data'))
def update_plot_time_score_scatter(data):
    movies = read_dataframe_from_store(data, 'movies')
    return create_time_score_scatter(movies)

@app.callback(Output('plot-budget-score-scatter', 'figure'), Input('data-store', 'data'))
def update_plot_budget_score_scatter(data):
    movies = read_dataframe_from_store(data, 'movies')
    return create_budget_score_scatter(movies)

@app.callback(Output('plot-genre-distribution', 'figure'), Input('data-store', 'data'))
def update_plot_genre_distribution(data):
    movies = read_dataframe_from_store(data, 'movies')
    movies = movies.dropna(subset=['budget', 'score'], how='any')
    return create_genre_distribution(movies, 'genre')

@app.callback(Output('table-movie', 'children'), [Input('data-store', 'data'), Input('toggle-table-movie', 'on')])
def update_table(data, toggle_value):
    _movies = read_dataframe_from_store(data, 'movies')
    if toggle_value:
        # Bottom 20 movies
        movies = _movies.sort_values(by='score', ascending=True).head(20)
    else:
        # Top 20 movies
        movies = _movies.sort_values(by='score', ascending=False).head(20)
    return create_movie_table(movies)
