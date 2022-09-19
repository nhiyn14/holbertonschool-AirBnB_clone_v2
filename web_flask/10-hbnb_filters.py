#!/usr/bin/python3
"""
script that starts a Flask web application
listening on 0.0.0.0, port 5000
use storage for fetching data from the storage engine
remove current SQLAlchemy Session after each request
/hbnb_filters: display templates/10-hbnb_filters.html
State, City and Amenity loaded from DBStorage and sorted by name
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def remove_alchemy_sess(self):
    """Remove current SQLAlchemy Session after each request"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def static_web():
    """Display static web content"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
