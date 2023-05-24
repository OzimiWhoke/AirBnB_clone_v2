#!/usr/bin/python3
"""a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def show_c(text):
    processed_text = text.replace('_', ' ')
    return 'C {}'.format(processed_text)


@app.route('/python/', methods=['GET'], strict_slashes=False)
@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
def show_python(text="is cool"):
    processed_text = text.replace('_', ' ')
    return 'Python {}'.format(processed_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

