@app.route("/chat", methods=["POST"])
def chat():
    data = request.json

    messages = data.get("messages", [])
    student = data.get("student")

    if not messages:
        return jsonify({"reply": "Napíš správu 🙂"})

    # bezpečný text študenta
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

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                *messages
            ]
        )

        return jsonify({"reply": response.choices[0].message.content})

    except Exception as e:
        return jsonify({"reply": f"Chyba backendu: {str(e)}"}), 500
