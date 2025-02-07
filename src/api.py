from flask import Flask, jsonify, request

from src.utils import add

app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"})


@app.route("/sum", methods=["POST"])
def sum_numbers():
    data = request.json
    try:
        result = add(data["a"], data["b"])
        return jsonify({"result": result})
    except (KeyError, ValueError) as e:
        return jsonify({"error": str(e)}), 400
