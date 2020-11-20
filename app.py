from flask import Flask
from lexer import parser
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/compiler')
def compiler():
    # try:
    print(parser())
    return 'h'
    # except:
    #     print("no funciono", parser())
    #     return 'chale'


@app.route('/compiler2')
def compiler_aux():
    result = os.system('python lexer.py')
    if 0 == result:
        print("funciona")
        return 'funciona'
    else:
        print("no funciona")
        return 'hola'
    # return parser()

# @app.route('/exceptions')
# def exceptions():
#     with open('parser.py') as f;
#     script = f.read()
#     try:
#         exec(script)
#     except EOFError as e:
#         print('uwu', e)
