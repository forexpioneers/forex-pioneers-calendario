# app.py
from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# La tua API Key di Financial Modeling Prep
API_KEY = "thrUZxd3FY9PbuoKSi5hsgLFNEQhHEm6"

# Endpoint dell'API per il calendario economico
FMP_URL = f"https://financialmodelingprep.com/api/v3/economic_calendar?apikey={API_KEY}"

@app.route("/calendario.json")
def calendario():
    try:
        response = requests.get(FMP_URL)
        data = response.json()

        eventi = []
        for evento in data[:10]:  # Limita ai primi 10 eventi
            eventi.append({
                "data": evento.get("date", "N/A"),
                "evento": evento.get("event", "N/A"),
                "paese": evento.get("country", "N/A")
            })

        return jsonify(eventi)

    except Exception as e:
        return jsonify({"errore": str(e)}), 500

if __name__ == "__main__":
    # Host e porta configurabili per Render
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))



