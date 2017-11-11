#!/bin/bash
. ./__kill_flask.sh
rm nohup.out

export FLASK_APP=start.py
nohup python3 -m flask run --host=0.0.0.0 &


