from flask import Flask, request, jsonify
import csv
from flask import send_from_directory
import os

app = Flask(__name__)

API_KEY = "mysecretkey123"
CSV_FILE = "users.csv"

def load_users():
    users = {}
    try:
        with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                users[row['userID']] = int(row['kor'])
    except Exception:
        pass
    return users

@app.route("/get_kor", methods=["POST"])
def get_kor():
    if not request.is_json:
        return jsonify("Hibás kérésformátum, JSON szükséges."), 400

    print("Érkezett kérés:", request.method, request.data)
    
    data = request.get_json()
    api_key = data.get("api_key")
    user_id = data.get("userID")

    if api_key != API_KEY:
        return jsonify("hibás-api-key"), 403

    if not user_id:
        return jsonify("Hiányzó userID"), 400

    users = load_users()
    if user_id in users:
        return jsonify(users[user_id])
    else:
        return jsonify("userID nem létezik"), 404

@app.route("/openapi.json")
def serve_openapi():
    return send_from_directory(os.getcwd(), "openapi.json", mimetype="application/json")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
