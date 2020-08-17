from flask import (Flask, render_template, redirect, request, flash, session, jsonify)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def api():
    return {
        'userId': 1,
        'title': 'Flask React Application',
        'completed': False
    }