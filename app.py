#!/usr/bin/env python3
from subprocess import check_output as run
import logging
from flask import Flask, request

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

command = ["dig","+short","ch","txt","whoami.cloudflare","@1.1.1.1"]

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def ip(path):
    output= run(command,universal_newlines=True)
    app.logger.info(f"ip from request: {request.remote_addr}")
    app.logger.info(f"public ip: {output}")
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
