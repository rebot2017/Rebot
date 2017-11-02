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
@app.route('/api/<script>/<username>')
def call(script, username):
    print(sys.path)
    args = request.args.get("params")
    print("%s for %s called with params: %s"%(script, username, args))
    args = args.replace("+", " ")
    try:
        mod = importlib.import_module("chatscripts.%s_%s"%(username, script))
        mod = importlib.reload(mod)
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
    os.system("echo '/home %s(rw,no_subtree_check,no_root_squash,sync)' >> /etc/exports"%address)
    os.system("systemctl restart nfs-kernel-server")
    return "ok" 

@app.route("/reset/<username>")
def reset_user(username):
    import os
    print("resetting: %s"%username)
    os.system("rm -Rf /home/%s/.local"%username)
    return "ok"
