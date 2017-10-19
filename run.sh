#!/bin/bash
export FLASK_APP=start.py
nohup python3 -m flask run --host=0.0.0.0
