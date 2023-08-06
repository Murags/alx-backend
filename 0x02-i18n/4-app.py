#!/usr/bin/env python3
"""_summary_"""

from flask import Flask, render_template
from flask_babel import Babel, request


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


@app.route('/', strict_slashes=False)
def home() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    return render_template("4-index.html")


@babel.localeselector
def get_locale() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
