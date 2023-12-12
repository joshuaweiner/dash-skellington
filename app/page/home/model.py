#!/usr/bin/env python

""" Model
"""

import pandas as pd 


credit_df = pd.read_csv(config.APP_DATA_DIR / 'references.csv').assign(
    name=lambda df: df.apply(lambda x: f"[{x['name']}]({x['url']})", axis=1)
)


