#!/usr/bin/env python

"""
Creates a scatter plot with budget on x-axis and score on y-axis.
"""

import pandas as pd
import plotly.express as px


def create_budget_score_scatter(df):
    return px.scatter(df, x='budget', y='score', title='Budget vs Score', trendline='ols',
                      trendline_color_override='black',
                      labels={'movie': 'Movie', 'budget': 'Budget (USD)', 'score': 'Score'})
                     
