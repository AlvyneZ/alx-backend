#!/usr/bin/env python3
"""
4-app.py - Starts a translated flask app
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Configuration object for Flask Babel
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app: Flask = Flask(__name__)
app.config.from_object(Config)
babel: Babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Gets the best match for supported languages

    Returns:
        str: best language match
    """
    queries = request.query_string.decode('utf-8').split('&')
    query_table = {}
    for query in queries:
        if "=" in query:
            label, value = query.split("=")
            query_table.update({label: value})
    if ('locale' in query_table) and \
            (query_table['locale'] in app.config["LANGUAGES"]):
        return query_table['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def landing() -> str:
    """Outputs the landing page of the simple site

    Returns:
        str: landing page
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
