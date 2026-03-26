from flask import Flask, jsonify

app = Flask(__name__)

databaza = {
    "students": [
        {
            "id": 1,
            "name": "Marcus",
            "surname": "Martiš",
            "nickname": "gypsy crusader",
        },{
            "id": 20,
            "name": "Adrian",
            "surname": "Červenka",
            "nickname": "neger",
        }
    ]
}

@app.route("/")
def index():
    return jsonify({"message": "Ahoj backend funguje"})

@app.route("/api")
def api():
    return jsonify(databaza)

@app.route("/api/student/<int:student_id>")
def find_student(student_id):
    for student in databaza["students"]:
        if student["id"] == student_id:
            return jsonify(student)
        
    return jsonify({ "error": "not found" })
    

if __name__ == "__main__":
    app.run(debug=True)
