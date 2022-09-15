#!/usr/bin/python3
"""
a script upgrade from 5-number_template
/number_odd_or_even/<n>: display a HTML page only if n is int
H1 tag: “Number: n is even|odd” inside the tag BODY
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


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def n_odd_even(n):
    """Display H1 tag: “Number: n is even|odd"""
    if (isinstance(n, int) is True):
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
