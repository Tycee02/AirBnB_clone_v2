#!/usr/bin/python3
"""
Starts a flask web application
"""

from flask import Flask, render_template  # type: ignore
from models import *  # type: ignore
from models import storage  # type: ignore
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    states = storage.all("state")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
