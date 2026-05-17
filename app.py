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
    {"id": 4, "name": "Jana", "surname": "Horvathova", "nickname": "Jani", "age": 21},
    {"id": 5, "name": "Tomáš", "surname": "Bielik", "nickname": "Tomy", "age": 24},
    {"id": 6, "name": "Lucia", "surname": "Kralova", "nickname": "Lulu", "age": 20},
    {"id": 7, "name": "Filip", "surname": "Varga", "nickname": "Fifo", "age": 23},
    {"id": 8, "name": "Sofia", "surname": "Nemcova", "nickname": "Sofi", "age": 18},
    {"id": 9, "name": "Dominik", "surname": "Toth", "nickname": "Domi", "age": 26},
    {"id": 10, "name": "Ema", "surname": "Kovacikova", "nickname": "Emka", "age": 19}
]


# =========================
# VLASTNÝ SORT ALGORITMUS (BUBBLE SORT)
# =========================

def sort_students(students, sort_type):

    n = len(students)

    for i in range(n):
        for j in range(0, n - i - 1):

            a = students[j]
            b = students[j + 1]

            swap = False

            # ===== NAME A-Z =====
            if sort_type == "name_asc":
                swap = a["name"].lower() > b["name"].lower()

            # ===== AGE ASC (najmladší) =====
            elif sort_type == "age_asc":
                swap = a["age"] > b["age"]

            # ===== AGE DESC (najstarší) =====
            elif sort_type == "age_desc":
                swap = a["age"] < b["age"]

            if swap:
                students[j], students[j + 1] = students[j + 1], students[j]

    return students


# =========================
# API ENDPOINT
# =========================

@app.route("/api", methods=["GET"])
def get_students():

    sort_type = request.args.get("sort", "name_asc")

    sorted_students = sort_students(students_db.copy(), sort_type)

    return jsonify(sorted_students)


# =========================
# CHAT (ak ho používaš)
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

    return jsonify({
        "reply": f"Chat funguje. Vybraný študent: {student_text}"
    })


# =========================
# RUN
# =========================

if __name__ == "__main__":
    app.run(debug=True)
