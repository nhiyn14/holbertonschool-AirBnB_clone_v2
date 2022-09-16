#!/usr/bin/python3
"""
script that starts a Flask web application
listening on 0.0.0.0, port 5000
use storage for fetching data from the storage engine
remove current SQLAlchemy Session after each request
/cities_by_states: display 8-cities_by_states.html
<H1>States</H1>
<UL> sorted by name (A->Z)
<LI>State: <state.id>: <B><state.name></B>
<UL> sorted by name (A->Z)
<LI>City: <city.id>: <B><city.name></B></LI>
</UL>
</LI>
</UL>
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def remove_alchemy_sess(self):
    """Remove current SQLAlchemy Session after each request"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def state_list():
    """Display list of States AND Cities within"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
