from flask import Flask
from flask import request
from config import script_loc
import json
import importlib
import sys
if script_loc not in sys.path:
    sys.path.append(script_loc)
import chatscripts.gscript
import chatscripts.yfscript
import chatscripts.wikiscript
import chatscripts.bookdeposcript

def objToStr(obj):
    string = ""
    for key in obj:
        string+= key + ": " + obj[key] + '\n'
    return string
app = Flask(__name__)

@app.route('/gscript')
def gscript():
    args = request.args.get("params")
    print("gscript called with params: %s"%args)
    args = args.replace("+", " ")
    importlib.reload(chatscripts.gscript)
    obj = chatscripts.gscript.gm_search(args)
    return json.dumps(obj)

@app.route('/yfscript')
def yfscript():
    args = request.args.get("params")
    print("yfscript called with params: %s"%args)
    args = args.replace("+", " ")
    importlib.reload(chatscripts.yfscript)
    print("args, "+args)
    obj = chatscripts.yfscript.get_ticker_data(args)
    return objToStr(obj)

@app.route('/wikiscript')
def wikiscript():
    args = request.args.get("params")
    print("wikiscript called with params: %s"%args)
    args = args.replace("+", " ")
    importlib.reload(chatscripts.wikiscript)
    obj = chatscripts.wikiscript.wiki_search(args)
    return objToStr(obj)

@app.route('/bookdeposcript')
def bdscript():
    args = request.args.get("params")
    print("bdscript called with params: %s"%args)
    args = args.replace("+", " ")
    importlib.reload(chatscripts.bookdeposcript)
    obj = chatscripts.bookdeposcript.bookdepo_search(args)
    return json.dumps(obj)

@app.route('/')
def hello_world():
    return "hello world"

