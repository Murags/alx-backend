#!/usr/bin/env python3
"""_summary_"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    return render_template("2-index.html")



if __name__ == "__main__":
    app.run()
