#!/usr/bin/python3
"""
script that starts a Flask web application
listening on 0.0.0.0, port 5000
use storage for fetching data from the storage engine
remove current SQLAlchemy Session after each request
display 9-states.html
/states:
H1 tag: “States”
UL tag: with the list of all State sorted by name (A->Z) tip
LI tag: State: <state.id>: <B><state.name></B>

/states/<id>:
If a State object is found with this id:
H1 tag: “State: ”
H3 tag: “Cities:”
UL tag: with the list of City objects linked to the State sorted by name (A->Z)
LI tag: description of one City: <city.id>: <B><city.name></B>
Otherwise:
H1 tag: “Not found!”
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def remove_alchemy_sess(self):
    """Remove current SQLAlchemy Session after each request"""
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states_list", strict_slashes=False)
def state_list():
    """Display list of States"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route("/states/<string:id>", strict_slashes=False)
def state_city_list(id=None):
    """Display States AND Cities within"""
    states = storage.all(State)
    if id is not None:
        state_id = "State." + id
    return render_template('9-states.html',
                           state_id=state_id, states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
