#!/usr/bin/python3
"""
1-hbnb_route.py adds

/c/<text>: display C followed by the value of text
replace underscore (in text) with a space
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB!"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Display C + text"""
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
