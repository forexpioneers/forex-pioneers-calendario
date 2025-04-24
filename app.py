import os
from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

API_KEY = "thrUZxd3FY9PbuoKSi5hsgLFNEQhHEm6"
FMP_URL = f"https://financialmodelingprep.com/api/v3/economic_calendar?apikey={API_KEY}"

@app.route("/calendario.json")
def calendario():
    try:
        response = requests.get(FMP_URL)
        data = response.json()

        # Verifica se i dati sono una lista
        if isinstance(data, list):
            eventi = []
            for evento in data[:10]:  # Limita ai primi 10 eventi
                eventi.append({
                    "data": evento.get("date", "N/A"),
                    "evento": evento.get("event", "N/A"),
                    "paese": evento.get("country", "N/A")
                })
            return jsonify(eventi)
        else:
            # Se i dati non sono una lista, ritorna un errore
            return jsonify({"errore": "I dati dell'API non sono nel formato previsto"}), 500
    except Exception as e:
        return jsonify({"errore": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)


