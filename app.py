import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        "message": "Hello from my GitOps pipeline!",
        "pod": socket.gethostname(),
        "version": os.environ.get("APP_VERSION", "dev"),
    })

@app.route("/healthz")
def healthz():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
