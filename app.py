
from flask import Flask, jsonify

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "nazwa": "Klawiatura mechaniczna", "kategoria": "akcesoria", "cena": 349.99, "opis": "Podswietlenie RGB"},
    {"id": 2, "nazwa": "Mysz bezprzewodowa", "kategoria": "akcesoria", "cena": 129.00, "opis": "4000 DPI"},
    {"id": 3, "nazwa": "Monitor 27 cali", "kategoria": "monitory", "cena": 1099.00, "opis": "IPS, 144 Hz"},
    {"id": 4, "nazwa": "Sluchawki nauszne", "kategoria": "audio", "cena": 449.00, "opis": "ANC, 40 h pracy"},
    {"id": 5, "nazwa": "Hub USB-C", "kategoria": "akcesoria", "cena": 199.00, "opis": "HDMI, USB-A, SD"},
]

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/api/products")
def products():
    return jsonify(PRODUCTS)

@app.route("/api/products/<int:product_id>")
def product(product_id):
    item = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if item is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(item)

if __name__ == "__main__":
    app.run(debug=True)
