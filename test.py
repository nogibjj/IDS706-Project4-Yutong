#!/usr/bin/env python
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    print("envfile: " + os.getenv("OPENAI_API_KEY"))
    app.run(port = 8080, host = '127.0.0.1', debug = True)
