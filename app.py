from flask import Flask
from lexer import parser
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/compiler')
def compiler():
    print(parser())
    return 'Holis'