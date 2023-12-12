#!/usr/bin/env python

""" 
Creates a pie chart showing the distribution of movie genres.
"""

import pandas as pd
import plotly.express as px


def create_genre_distribution(df, genre_column='genre'):
    genre_counts = df[genre_column].value_counts()
    return px.pie(
        genre_counts,
        values=genre_counts.values,
        names=genre_counts.index,
        title='Movie Genre Distribution'
    )
