#!/usr/bin/env python3
"""
0-app.py - Starts a simple flask app
"""
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """Configuration object for Flask Babel
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app: Flask = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def landing() -> str:
    """Outputs the landing page of the simple site

    Returns:
        str: landing page
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
