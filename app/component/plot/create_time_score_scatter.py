#!/usr/bin/env python

"""
Creates a scatter plot with time (year) on x-axis and score on y-axis.
"""

import pandas as pd
import plotly.express as px
from plotly.validator_cache import ValidatorCache

def create_time_score_scatter(df):
    score_threshold = df['score'].quantile(0.9)
    df['highlight'] = df['score'] >= score_threshold
    return px.scatter(
        df, x='year', y='score',
        color='highlight', title="Movie Scores Over Time", hover_name='name', labels={'highlight': 'Top 10%'}
    )
