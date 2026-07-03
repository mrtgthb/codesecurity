from flask import Flask, jsonify
import os
import platform

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({
        "message": "Sample container app for security scanning tests",
        "hostname": platform.node(),
        "python_version": platform.python_version(),
    })


@app.route("/healthz")
def healthz():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
