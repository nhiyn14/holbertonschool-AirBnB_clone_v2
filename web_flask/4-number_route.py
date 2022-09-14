#!/usr/bin/python3
"""
a script upgrade from 3-python_route.py
/number/<n>: display “n is a number” only if n is int
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
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text='is_cool'):
    """Display Python + text"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def n_is_int(n):
    """Display “n is a number” only if n is int"""
    if (isinstance(n, int) is True):
        return "n is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
