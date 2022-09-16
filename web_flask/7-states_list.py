#!/usr/bin/python3
"""
script that starts a Flask web application
listening on 0.0.0.0, port 5000
use storage for fetching data from the storage engine
remove current SQLAlchemy Session after each request
/states_list: display a HTML page
H1 tag: “States”
UL tag: list all State objects in DBStorage sorted by name (A->Z)
LI tag: description of one State: <state.id>: <B><state.name></B>
must use the option strict_slashes=False in your route definition
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)

@app.teardown_appcontext
def remove_alchemy_sess(self):
    """Remove current SQLAlchemy Session after each request"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    """Display list of States"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
