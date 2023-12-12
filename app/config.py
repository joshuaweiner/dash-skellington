#!/usr/bin/env python

""" Dash App Configuration
"""

from types import SimpleNamespace
from pathlib import Path

import dash_bootstrap_components as dbc


# Define the root directory of the project
_PROJECT_ROOT = Path(__file__).resolve().parent

# Data directory for storing data files like CSVs
_APP_DATA_DIR = _PROJECT_ROOT / 'data'

# Specific path for the movies CSV file
_APP_DATA_SRC = _APP_DATA_DIR / 'movies.csv'

# Assets directory for storing static files like images, JS, CSS
_APP_ASSETS_DIR = _PROJECT_ROOT / 'asset'

# Pages directory for storing HTML or template files
_APP_PAGES_DIR = _PROJECT_ROOT / 'page'


config = SimpleNamespace(
    DASH_APP_NAME = 'Dash-Skellington',

    PROJECT_ROOT = _PROJECT_ROOT,

    APP_DATA_DIR = _APP_DATA_DIR,
    APP_DATA_SRC = _APP_DATA_SRC,

    APP_ASSETS_DIR = _APP_ASSETS_DIR,

    APP_PAGES_DIR = _APP_PAGES_DIR,

    APP_TITLE = 'Dash-Skellington',

    APP_UPDATE_TITLE = 'Loading...',

    CALLBACK_EXCEPTIONS = True,  # Use `True` for multi-page applications

    APP_STYLESHEETS = [
        'https://fonts.googleapis.com/css2?family=Inconsolata&display=swap',
        'https://fonts.googleapis.com/css2?family=Roboto&display=swap',
        dbc.themes.FLATLY,
    ],

    APP_DEBUG = True,
    APP_HOST = '127.0.0.1',
    APP_PORT = '7000',
)
