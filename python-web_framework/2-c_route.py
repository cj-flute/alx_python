"""
    A script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def text(text):
    return f'C {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
