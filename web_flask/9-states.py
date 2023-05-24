#!/usr/bin/python3
"""a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


@app.route('/states', methods=['GET'], strict_slashes=False)
def states():
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', methods=['GET'], strict_slashes=False)
def states_by_id(id):
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-states_by_id.html', state=state, cities=cities)
    else:
        return render_template('9-not_found.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
