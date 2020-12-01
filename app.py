from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/<name>')
def hello_page(name):
    return 'hello ' + name


@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return 'Niilber: %d' % (number1 + number2)


@app.route('/post', methods=['GET', 'POST'])
def post_entry():
    title = request.form['title']
    body = request.form['body']
    return render_template('details.html', title=title, body=body)
