from flask import Flask, request
from lexer import parser
import ast
import datetime
import os
import json 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/compiler')
def compiler():
    try:
        return parser()
    except Exception as e:
         return {'data': str(e), 'status': 400}

@app.route('/files', methods=['GET'])
def get_files():
    with open('files.json') as f:
        data = json.load(f)
    return data, 200

@app.route('/createFile')
def create_File():
    get_name = request.args.get("file", "")
    name = "{}".format(get_name)
    print("el nombre del programa es:", name)
    file_name = "pruebas/"+ name + ".txt"
    open(file_name, "w+")

    new_file = {
         "name": name,
         "createdAt": str(datetime.datetime.now()),
         "path": file_name            
    }
    n = None
    data = None
    
    with open('files.json') as f:
        data = json.load(f)
        data['files'].append(new_file)
        n = data
        p_json = json.dumps(n)
        print(p_json, file=open("files.json", "w"))
        
    return {"data": n}



@app.route('/compiler2')
def compiler_aux():
    result = os.system('python lexer.py')
    if 0 == result:
        print("funciona")
        return parser()
    else:
        #print("no funciona")
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
