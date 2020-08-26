"""Playlist creator."""
import os
import requests
from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session, jsonify)
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Location, connect_to_db, db

import google_api





app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("index.html", flask_token="Hello world")


if __name__ == "__main__":
    app.debug = True
    # app.debug = False

    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)
    
    DebugToolbarExtension(app)
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False #for error: AttributeError: 'Request' object has no attribute 'is_xhr'

    app.run(port=5000, host='0.0.0.0')
    # app.run() deployment