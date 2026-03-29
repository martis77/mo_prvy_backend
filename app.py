from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# CORS povolí tvojmu JavaScriptu sťahovať dáta z tohto backendu
CORS(app)

# Databáza študentov (zoznam slovníkov)
students_db = [
    {"id": 1, "name": "Marcus", "surname": "Martis", "nickname": "maro", "image": "https://i.pravatar.cc/150?img=1"},
    {"id": 2, "name": "Adrian", "surname": "Cervenka", "nickname": "adi", "image": "https://i.pravatar.cc/150?img=2"},
    {"id": 3, "name": "Peter", "surname": "Novak", "nickname": "peto", "image": "https://i.pravatar.cc/150?img=3"},
    {"id": 4, "name": "Jana", "surname": "Kovacova", "nickname": "jani", "image": "https://i.pravatar.cc/150?img=4"},
    {"id": 5, "name": "Tomas", "surname": "Hrasko", "nickname": "tomi", "image": "https://i.pravatar.cc/150?img=5"},
    {"id": 6, "name": "Eva", "surname": "Biela", "nickname": "evka", "image": "https://i.pravatar.cc/150?img=6"},
    {"id": 7, "name": "Marek", "surname": "Urban", "nickname": "marek", "image": "https://i.pravatar.cc/150?img=7"},
    {"id": 10, "name": "Nina", "surname": "Polakova", "nickname": "nina", "image": "https://i.pravatar.cc/150?img=10"},
    {"id": 8, "name": "Simona", "surname": "Zelena", "nickname": "simi", "image": "https://i.pravatar.cc/150?img=8"},
    {"id": 9, "name": "David", "surname": "Toth", "nickname": "davo", "image": "https://i.pravatar.cc/150?img=9"}
]

# 1. Route - Hlavná stránka
@app.route("/")
def index():
    return "Vitaj! Môj Flask backend funguje správne. Pre zoznam študentov choď na /api"

# 2. Route - Všetci študenti (JSON pole)
@app.route("/api")
def get_all_students():
    return jsonify(students_db)

# 3. Route - Jeden študent podľa ID
@app.route("/api/student/<int:student_id>")
def get_one_student(student_id):
    # Vyhľadá študenta v zozname podľa id
    student = next((s for s in students_db if s["id"] == student_id), None)
    
    if student:
        return jsonify(student)
    else:
        return jsonify({"error": "Študent s týmto ID neexistuje"}), 404

if __name__ == "__main__":
    # Spustenie servera na tvojom počítači
    app.run(debug=True)
