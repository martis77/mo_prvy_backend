from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

students_db = [
    {"id": 1, "name": "Marcus", "surname": "Martis", "nickname": "maro"},
    {"id": 2, "name": "Adrian", "surname": "Cervenka", "nickname": "adi"},
    {"id": 3, "name": "Peter", "surname": "Novak", "nickname": "peto"},
    {"id": 4, "name": "Jana", "surname": "Kovacova", "nickname": "jani"},
    {"id": 5, "name": "Tomas", "surname": "Hrasko", "nickname": "tomi"},
    {"id": 6, "name": "Eva", "surname": "Biela", "nickname": "evka"},
    {"id": 7, "name": "Marek", "surname": "Urban", "nickname": "marek"},
    {"id": 8, "name": "Simona", "surname": "Zelena", "nickname": "simi"},
    {"id": 9, "name": "David", "surname": "Toth", "nickname": "davo"},
    {"id": 10, "name": "Nina", "surname": "Polakova", "nickname": "nina"}
]

@app.route("/")
def home():
    return "Backend beží!"

@app.route("/api")
def get_students():
    return jsonify(students_db)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])
    student = data.get("student")

    if not messages:
        return jsonify({"reply": "Napíš správu 🙂"})

    student_text = ""
    if student:
        student_text = f"Aktuálne pracuješ so študentom: {student.get('name')} {student.get('surname')} ({student.get('nickname')})"

    students_info = "\n".join([
        f"{s['id']}: {s['name']} {s['surname']} ({s['nickname']})"
        for s in students_db
    ])

    system_prompt = f"""
Si školský AI chatbot.

{student_text}

Zoznam študentov:
{students_info}

Odpovedaj stručne po slovensky.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                *messages
            ]
        )

        return jsonify({
            "reply": response.choices[0].message.content
        })

    except Exception as e:
        return jsonify({"reply": f"Chyba: {str(e)}"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
