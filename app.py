from flask import Flask, jsonify

app = Flask(__name__)

databaza = {
    "students": [
        {"id": 1, "name": "Marcus", "surname": "Martis", "nickname": "maro", "image": "https://i.pravatar.cc/150?img=1"},
        {"id": 2, "name": "Adrian", "surname": "Cervenka", "nickname": "adi", "image": "https://i.pravatar.cc/150?img=2"},
        {"id": 3, "name": "Peter", "surname": "Novak", "nickname": "peto", "image": "https://i.pravatar.cc/150?img=3"},
        {"id": 4, "name": "Jana", "surname": "Kovacova", "nickname": "jani", "image": "https://i.pravatar.cc/150?img=4"},
        {"id": 5, "name": "Tomas", "surname": "Hrasko", "nickname": "tomi", "image": "https://i.pravatar.cc/150?img=5"},
        {"id": 6, "name": "Eva", "surname": "Biela", "nickname": "evka", "image": "https://i.pravatar.cc/150?img=6"},
        {"id": 7, "name": "Marek", "surname": "Urban", "nickname": "marek", "image": "https://i.pravatar.cc/150?img=7"},
        {"id": 8, "name": "Simona", "surname": "Zelena", "nickname": "simi", "image": "https://i.pravatar.cc/150?img=8"},
        {"id": 9, "name": "David", "surname": "Toth", "nickname": "davo", "image": "https://i.pravatar.cc/150?img=9"},
        {"id": 10, "name": "Nina", "surname": "Polakova", "nickname": "nina", "image": "https://i.pravatar.cc/150?img=10"}
    ]
}

@app.route("/")
def index():
    return "Ahoj backend funguje"

@app.route("/api")
def api():
    return jsonify(databaza["students"])

@app.route("/api/student/<int:student_id>")
def find_student(student_id):
    for student in databaza["students"]:
        if student["id"] == student_id:
            return jsonify(student)

    return jsonify({"error": "not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
