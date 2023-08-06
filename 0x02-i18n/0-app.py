#!/usr/bin/env python3
"""_summary_"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home() -> str:
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
