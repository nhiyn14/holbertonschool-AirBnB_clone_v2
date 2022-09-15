#!/usr/bin/python3
"""
a script upgrade from 4-number_route.py
/number_template/<n>: display a HTML page only if n is int
h1 tag: “Number: n” inside the tag body
"""
from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text='is_cool'):
    """Display Python + text"""
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def n_is_int(n):
    """Display “n is a number” only if n is int"""
    if (isinstance(n, int) is True):
        return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_html_template(n):
    """Display h1 tag: “Number: n” if n is int"""
    if (isinstance(n, int) is True):
        return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
