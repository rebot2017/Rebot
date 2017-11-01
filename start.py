from flask import Flask
from flask import request
from config import script_loc
import json
import importlib
import sys
if script_loc not in sys.path:
    sys.path.append(script_loc)
import chatscripts
import middleware
def objToStr(obj):
    string = ""
    for key in obj:
        string+= key + ": " + obj[key] + '\n'
    return string

app = Flask(__name__)
app.wsgi_app = middleware.MiddleWare(app.wsgi_app)
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
    try:
        mod = importlib.import_module("chatscripts.team%s_gscript"%team_id)
        mod = importlib.reload(mod)
        obj = mod.call_api(args)
        return json.dumps(obj)
    except ImportError:
        return json.dumps([{"type": "string", "data": "Ooops! You have not committed the script!"}])
    except:
        return json.dumps([{"type": "string", "data": "Ooops! Your code looks like it needs some polishing. Try asking for help (:"}])
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
def team_yfscript(team_id):
    args = request.args.get("params")
    print("yfscript for team {%s} called with params: %s"%(team_id,args))
    args = args.replace("+", " ")
    try:
        mod = importlib.import_module("chatscripts.team%s_yfscript"%team_id)
        importlib.reload(mod)
        print("args, "+args)
        obj = mod.call_api(args)
        return json.dumps(obj)
    except ImportError:
        return json.dumps([{"type": "string", "data": "Ooops! You have not committed the script!"}])
    except:
        return json.dumps([{"type": "string", "data": "Ooops! Your code looks like it needs some polishing. Try asking for help (:"}])

@app.route('/wikiscript')
def wikiscript():
    args = request.args.get("params")
    print("wikiscript called with params: %s"%args)
    args = args.replace("+", " ")
    importlib.reload(chatscripts.wikiscript)
    obj = chatscripts.wikiscript.call_api(args)
    return json.dumps(obj)


@app.route('/wikiscript/<int:team_id>')
def team_wikiscript(team_id):
    args = request.args.get("params")
    print("wikiscript for team {%s} called with params: %s"%(team_id,args))
    args = args.replace("+", " ")
    try:
        mod = importlib.import_module("chatscripts.team%s_bookdeposcript"%team_id)
        importlib.reload(mod)
        print("args, "+args)
        obj = mod.call_api(args)
        return json.dumps(obj)
    except ImportError:
        return json.dumps([{"type": "string", "data": "Ooops! You have not committed the script!"}])
    except:
        return json.dumps([{"type": "string", "data": "Ooops! Your code looks like it needs some polishing. Try asking for help (:"}])




@app.route('/bookdeposcript')
def bdscript():
    args = request.args.get("params")
    print("bdscript called with params: %s"%args)
    args = args.replace("+", " ")
    importlib.reload(chatscripts.bookdeposcript)
    obj = chatscripts.bookdeposcript.call_api(args)
    return json.dumps(obj)


@app.route('/bookdeposcript/<int:team_id>')
def team_bdscript(team_id):
    args = request.args.get("params")
    print("bdscript for team {%s} called with params: %s"%(team_id,args))
    args = args.replace("+", " ")
    try:
        mod = importlib.import_module("chatscripts.team%s_bookdeposcript"%team_id)
        importlib.reload(mod)
        print("args, "+args)
        obj = mod.call_api(args)
        return json.dumps(obj)
    except ImportError:
        return json.dumps([{"type": "string", "data": "Ooops! You have not committed the script!"}])
    except:
        return json.dumps([{"type": "string", "data": "Ooops! Your code looks like it needs some polishing. Try asking for help (:"}])



@app.route('/')
def hello_world():
    return "hello world"

@app.route("/ipaddr/<address>")
def add_ip(address):
    import os
    print("address:%s"%address)
    sh_call = "echo /home/chatscripts %s(rw,no_subtree_check,no_root_squash,sync) >> /etc/exports"
    print(sh_call%address)
    os.system("echo '/home/chatscripts %s(rw,no_subtree_check,no_root_squash,sync)' >> /etc/exports"%address)
    os.system("systemctl restart nfs-kernel-server")
    return "ok" 
