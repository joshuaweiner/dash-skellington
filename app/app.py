""" dash.Dash(), Flask Service Initialization
"""

import dash
import dash_bootstrap_components as dbc

from config import config


app = dash.Dash(
    name=config.DASH_APP_NAME,
    assets_folder=config.APP_ASSETS_DIR,
    title=config.APP_TITLE,
    update_title=config.APP_UPDATE_TITLE,
    suppress_callback_exceptions=config.CALLBACK_EXCEPTIONS,
    external_stylesheets=config.APP_STYLESHEETS,
)
