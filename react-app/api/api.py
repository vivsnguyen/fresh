import time
from flask import (Flask, render_template, redirect, request, flash, session)

app = Flask(__name__)

@app.route("/time", methods=["GET"])
def get_current_time():
    return {'time': time.time()}