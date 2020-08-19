import time
from flask import (Flask, render_template, redirect, request, flash, session)

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/time", methods=["GET"])
def get_current_time():
    return {'time': time.time()}
