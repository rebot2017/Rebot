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
import chatscripts

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
    obj = chatscripts.gscript.call_api(args)
    return json.dumps(obj)


@app.route('/gscript/<int:team_id>')
def team_gscript(team_id):
    args = request.args.get("params")
    print("gscript for team {%s} called with params: %s"%(team_id, args))
    args = args.replace("+", " ")
    mod = importlib.import_module("chatscripts.team%s_gscript"%team_id)
    mod = importlib.reload(mod)
    obj = mod.call_api(args)
    return json.dumps(obj)

@app.route('/yfscript')
def yfscript():
    args = request.args.get("params")
    print("yfscript called with params: %s"%args)
    args = args.replace("+", " ")
    importlib.reload(chatscripts.yfscript)
    print("args, "+args)
    obj = chatscripts.yfscript.call_api(args)
    return json.dumps(obj)

@app.route('/yfscript/<int:team_id>')
def yfscript(team_id):
    args = request.args.get("params")
    print("yfscript called with params: %s"%args)
    args = args.replace("+", " ")
    mod = importlib.import_module("chatscripts.team%s_yfscript"%team_id)
    importlib.reload(mod)
    print("args, "+args)
    obj = mod.call_api(args)
    return json.dumps(obj)

@app.route('/wikiscript')
def wikiscript():
    args = request.args.get("params")
    print("wikiscript called with params: %s"%args)
    args = args.replace("+", " ")
    importlib.reload(chatscripts.wikiscript)
    obj = chatscripts.wikiscript.call_api(args)
    return json.dumps(obj)

@app.route('/bookdeposcript')
def bdscript():
    args = request.args.get("params")
    print("bdscript called with params: %s"%args)
    args = args.replace("+", " ")
    importlib.reload(chatscripts.bookdeposcript)
    obj = chatscripts.bookdeposcript.call_api(args)
    return json.dumps(obj)

@app.route('/')
def hello_world():
    return "hello world"

