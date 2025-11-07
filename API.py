from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
DATA_FILE = "weer_data.json"

@app.route("/api/weer", methods=["POST"])
def post_weer():
    data = request.get_json()
    if not data:
        return jsonify({"error": "geen JSON"}), 400
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
    return jsonify({"ok": True})

@app.route("/api/weer", methods=["GET"])
def get_weer():
    if not os.path.exists(DATA_FILE):
        return jsonify({"error": "geen data"}), 404
    with open(DATA_FILE) as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
