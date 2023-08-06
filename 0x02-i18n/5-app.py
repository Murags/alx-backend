#!/usr/bin/env python3
"""_summary_"""

from flask import Flask, render_template, g
from flask_babel import Babel, request
from typing import Union, Dict


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    if g.user:
        username = g.user.get("name")
    else:
        username = None
    return render_template("5-index.html", username=username)


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


def get_user() -> Union[Dict, None]:
    """_summary_

    Returns:
        Union[Dict, None]: _description_
    """
    if request.args.get('login_as'):
        user_id = request.args.get('login_as')
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """_summary_
    """
    g.user = get_user()


if __name__ == "__main__":
    app.run()
