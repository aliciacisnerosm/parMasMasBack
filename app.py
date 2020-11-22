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

@app.route('/compiler', methods=['GET'])
def compiler():
    try:

        print(request.get_json())
        usr_input = request.args.get("input")
        file_name = request.args.get("name")

        filename = "pruebas/" + str(file_name) + ".txt"
        print(file_name)
       # print(parser(file_name))
        return parser(file_name), 200
    except Exception as e:
         print(parser(file_name))
         return str(e),  400

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

@app.route('/saveFile', methods=['POST'])
def save_file():
    try:
        print(request.get_json())
        req_data = request.get_json()
        file_text = req_data['file']
        file_name = req_data['name']

        filename = "pruebas/"+str(file_name) + ".txt"
        print(file_text, file=open(filename, "w"))
        
        print(file_text, file_name)
        return 'Archivo guardado!', 200
    except:
        return 'Error: No se pudo guardar el archivo', 400

@app.route('/readFile', methods=['GET'])
def read_file():
    try:
        get_name = request.args.get("file", "")
        name = "{}".format(get_name)
        print("el nombre del programa es:", name)
        f = open("pruebas/" + str(name) + ".txt", "r")
        n = f.read()

        return n
    except:
        return 'Error: No se pudo leer el archivo', 400
