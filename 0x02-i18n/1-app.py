#!/usr/bin/env python3
"""_summary_

    Returns:
        _type_: _description_
"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)

babel = Babel(app)


class Config(object):
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'fr'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def home() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
