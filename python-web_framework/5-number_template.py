"""
    A script that starts a Flask web application
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def texts(text):
    word = []
    text_list = list(text)
    for texts in range(len(text)):
        if text_list[texts] == '_':
            text_list[texts] = ' '
        word.append(text_list[texts])
    words = ''.join(word)
    return f'C {words}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/')
@app.route('/pyton')
def python(text=' is cool'):
    new_text = texts(text)
    if text == True:
        return 'Python' + text
    return 'Python' + new_text[1:]


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    if type(n) == int:
        return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if type(n) == int:
        return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
