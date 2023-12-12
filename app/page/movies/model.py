#!/usr/bin/env python

""" Page Model
"""

import pandas as pd

from config import config


class Clean:

    USE_COLUMNS = [
        'name',
        'rating',
        'genre',
        'year',
        'budget',
        'score',
        'country',
    ]

    def __init__(self, df):
        self.df = df.copy()

    def _preprocess(self):
        self.df = self.df[self.USE_COLUMNS]
        return 0

    def _process(self):
        self.df['rating'] = pd.Categorical(self.df['rating'])
        return 0

    def _postprocess(self):
        self.df.sort_values(
            by=['rating', 'score', 'name'],
            ascending=True, inplace=True
        )

        self.df = self.df.reset_index(drop=True)
        return 0

    def __call__(self):
        self._preprocess()
        self._process()
        self._postprocess()
        return self.df


def load_model_data():
    source_data = pd.read_csv(config.APP_DATA_SRC)
    clean_df = Clean(source_data)
    return clean_df()
