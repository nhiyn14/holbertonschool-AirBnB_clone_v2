#!/usr/bin/python3
"""
2-c_route.py adds
/python/<text>: display Python followed by the value of text
replace underscore (in text) with a space
default value of text is “is cool”
"""
from flask import Flask
from markupsafe import escape

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
