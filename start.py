from flask import Flask
from flask import request
from config import script_loc
import json
import sys
if script_loc not in sys.path:
    sys.path.append(script_loc)



app = Flask(__name__)

@app.route('/gscript')
def gscript():
    args = request.args.get("params")
    print("gscript called with params: %s"%args)
    args = args.replace("+", " ")
    from chatscripts.gscript import gm_search
    obj = gm_search(args)
    return json.dumps(obj)

@app.route('/yfscript')
def yfscript():
    print("yfscript")


@app.route('/')
def hello_world():
    return "hello world"
