#!/usr/bin/env python3
from subprocess import check_output as sub

from flask import Flask

app = Flask(__name__)

command = ["dig","+short","ch","txt","whoami.cloudflare","@1.1.1.1"]

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def ip(path):
    output= sub(command).decode('ascii')
    return output

if __name__ == '__main__':
    output= sub(command).decode('ascii')
    print(output)
    app.run(host='0.0.0.0', port=4000)
