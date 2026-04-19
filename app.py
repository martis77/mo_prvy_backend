from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Databáza študentov
students_db = [
    {"id": 1, "name": "Marcus", "surname": "Martis", "nickname": "maro", "image": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=400&h=400&fit=crop"},
    {"id": 2, "name": "Adrian", "surname": "Cervenka", "nickname": "adi", "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop"},
    {"id": 3, "name": "Peter", "surname": "Novak", "nickname": "peto", "image": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&h=400&fit=crop"},
    {"id": 4, "name": "Jana", "surname": "Kovacova", "nickname": "jani", "image": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&h=400&fit=crop"},
    {"id": 5, "name": "Tomas", "surname": "Hrasko", "nickname": "tomi", "image": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&h=400&fit=crop"},
    {"id": 6, "name": "Eva", "surname": "Biela", "nickname": "evka", "image": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400&h=400&fit=crop"},
    {"id": 7, "name": "Marek", "surname": "Urban", "nickname": "marek", "image": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&h=400&fit=crop"},
    {"id": 8, "name": "Simona", "surname": "Zelena", "nickname": "simi", "image": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400&h=400&fit=crop"},
    {"id": 9, "name": "David", "surname": "Toth", "nickname": "davo", "image": "https://images.unsplash.com/photo-1527980965255-d3b416303d12?w=400&h=400&fit=crop"},
    {"id": 10, "name": "Nina", "surname": "Polakova", "nickname": "nina", "image": "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=400&h=400&fit=crop"}
]

# ------------------------
# EXISTUJÚCE API
# ------------------------

@app.route("/")
def home():
    return "Backend beží! Použi /api alebo /chat"

@app.route("/api")
def get_students():
    return jsonify(students_db)

@app.route("/api/student/<int:sid>")
def get_student(sid):
    s = next((x for x in students_db if x["id"] == sid), None)
    return jsonify(s) if s else (jsonify({"error": "Nenájdený"}), 404)

# ------------------------
# AI CHATBOT
# ------------------------

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])

    # Prevod DB na text pre AI
    students_info = "\n".join([
        f"{s['id']}: {s['name']} {s['surname']} (prezývka: {s['nickname']})"
        for s in students_db
    ])

    system_prompt = f"""
Si školský AI chatbot.

Máš databázu študentov:
{students_info}

Pravidlá:
- odpovedaj stručne
- ak sa pýtajú na študentov, použi tieto dáta
- ak niečo nevieš, povedz to normálne
- odpovedaj po slovensky
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": system_prompt},
                *messages
            ]
        )

        return jsonify({
            "reply": response.choices[0].message.content
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------

if __name__ == "__main__":
    app.run(debug=True)
