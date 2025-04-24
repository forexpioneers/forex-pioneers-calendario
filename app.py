import os

from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/calendario.json")
def calendario():
    with open("dati_calendario.json", "r", encoding="utf-8") as f:
        dati = json.load(f)
    return jsonify(dati)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))



