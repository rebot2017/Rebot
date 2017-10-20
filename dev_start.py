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


app = Flask(__name__)



@app.route("/")
def welcome():
    str = "<h1>Available functions:</h1>"
    str += "<h3>reset notebook: /reset/<script>/<team_num> \n e.g. /reset/gscript/team1</h3> "
    str += "<h3>force pull from server: /gitpull</h3>"
    return str

@app.route("/reset/<string:script>/<string:team_id>")
def replace_nb(script, team_num):
    import os
    return_code = os.system("cp %s/archives/master/%s %s/%s/%s"%(script_loc, script, script_loc, team_num, script))
    return "return: "+ str(return_code)


@app.route("/gitpull")
def git_pull():
    import os
    return_code = os.system("git -C %s pull -f"%script_loc)
    return "return: " + str(return_code)