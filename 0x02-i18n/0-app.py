#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home() -> str:
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('index.html')

app.run()
