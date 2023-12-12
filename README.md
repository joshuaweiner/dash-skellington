# Dash-Skellington


### app.py 

This is where the core dash module exists. `dash.Dash()` uses flask
under the hood to serve the application.

We have made some adjustments to the default values of parameters. We
find that it is best to separate this file into a separate
configuration file that can be copied and re-used for future
applications. Please see `config.py` for a list of app configuration
values.


Reference: 
- https://dash.plotly.com/reference
- https://flask.palletsprojects.com/en/3.0.x/api/#application-object


### config.py

When there are opportunities to store configuration constants
`dash-skellington` opts to store these settings in separate files. To
store configuration variables we use a `types.SimpleNamespace` object.

Note, when developing multi-page apps use `suppress_callback_exceptions=True`

Reference: 
- https://docs.python.org/3/library/types.html#additional-utility-classes-and-functions
