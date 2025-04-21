# 1. szükséges importok
from flask import Flask, request, jsonify, send_from_directory
import csv
import os

# 2. Flask inicializálás
app = Flask(__name__)

# 3. API-kulcs konfiguráció
VALID_API_KEY = "mysecretkey123"

# 4. Életkor lekérdező végpont
@app.route("/get_kor", methods=["POST"])
def get_kor():
    data = request.get_json()
    if not data or "api_key" not in data or "userID" not in data:
        return jsonify("Hiányzó adat"), 400
    if data["api_key"] != VALID_API_KEY:
        return jsonify("hibás-api-key"), 403

    user_id = data["userID"]
    with open("users.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["userID"] == user_id:
                return jsonify(int(row["kor"])), 200

    return jsonify("userID nem létezik"), 404

# 5. openapi.json kiszolgálása
@app.route("/openapi.json")
def serve_openapi():
    return send_from_directory(os.getcwd(), "openapi.json", mimetype="application/json")

# 6. ai-plugin.json kiszolgálása a kötelező útvonalon
@app.route("/.well-known/ai-plugin.json")
def serve_plugin_manifest():
    return send_from_directory("plugin", "ai-plugin.json", mimetype="application/json")

# 7. alkalmazás indítása (Replit automatikusan hívja)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
