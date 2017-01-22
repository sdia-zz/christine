#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os
from flask import Flask
app = Flask(__name__)

APP_PORT = int(os.environ['APP_PORT'])



@app.route("/")
def hello():
    return "Hello World!"



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=APP_PORT)
