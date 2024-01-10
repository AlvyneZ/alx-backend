#!/usr/bin/env python3
"""
0-app.py - Starts a simple flask app
"""

from flask import Flask, render_template


app: Flask = Flask(__name__)


@app.route('/')
def landing() -> str:
    """Outputs the landing page of the simple site

    Returns:
        str: landing page
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
