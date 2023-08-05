#!/usr/bin/env python3

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)

babel = Babel(app)

class Config(object):
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'fr'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@app.route('/')
def home():

    return render_template("1-index.html")

app.run(debug=True)
