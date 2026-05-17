from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# =========================
# DÁTA
# =========================

students_db = [
    {"id": 1, "name": "Peter", "surname": "Novak", "nickname": "Peto", "age": 22},
    {"id": 2, "name": "Anna", "surname": "Kovacova", "nickname": "Anka", "age": 19},
    {"id": 3, "name": "Martin", "surname": "Mrkvicka", "nickname": "Majo", "age": 25},
]


# =========================
# VLASTNÝ SORT (BUBBLE SORT)
# =========================

def sort_students(students, sort_type):

    n = len(students)

    for i in range(n):
        for j in range(0, n - i - 1):

            a = students[j]
            b = students[j + 1]

            swap = False

            if sort_type == "name_asc":
                swap = a["name"].lower() > b["name"].lower()

            elif sort_type == "age_asc":
                swap = a["age"] > b["age"]

            elif sort_type == "age_desc":
                swap = a["age"] < b["age"]

            if swap:
                students[j], students[j + 1] = students[j + 1], students[j]

    return students


# =========================
# API - ŠTUDENTI
# =========================

@app.route("/api", methods=["GET"])
def get_students():

    sort_type = request.args.get("sort", "name_asc")

    sorted_students = sort_students(students_db.copy(), sort_type)

    return jsonify(sorted_students)


# =========================
# CHAT (NECHÁME BEZ ZMENY LOGIKY)
# =========================

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json

    messages = data.get("messages", [])
    student = data.get("student")

    if not messages:
        return jsonify({"reply": "Napíš správu 🙂"})

    if student:
        student_text = f"{student.get('name','')} {student.get('surname','')} ({student.get('nickname','')})"
    else:
        student_text = "Žiadny študent nebol vybraný"

    students_info = "\n".join([
        f"{s['id']}: {s['name']} {s['surname']} ({s['nickname']})"
        for s in students_db
    ])

    system_prompt = f"""
Si školský AI chatbot.

Vybraný študent: {student_text}

Zoznam študentov:
{students_info}

Odpovedaj stručne po slovensky.
"""

    return jsonify({
        "reply": "OK (chat zostáva rovnaký – sem máš svoj OpenAI kód)"
    })


# =========================
# RUN
# =========================

if __name__ == "__main__":
    app.run(debug=True)
