#!/usr/bin/env python

""" Utilities
"""

import io
import json
import pandas as pd


def read_dataframe_from_store(dataset: str, key: str) -> pd.DataFrame:
    return pd.read_json(io.StringIO(json.loads(dataset)[key])).copy()

def read_list_from_store(dataset: str, key: str) -> list:
    return json.loads(dataset)[key]
