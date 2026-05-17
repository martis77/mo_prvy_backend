const API_URL = "https://moj-prvy-backend-1.onrender.com";

let selectedStudent = null;
let messages = [];

// =========================
// NAČÍTANIE ŠTUDENTOV
// =========================

async function loadStudents(sortType = "name_asc") {

    const res = await fetch(`${API_URL}/api?sort=${sortType}`);
    const data = await res.json();

    const container = document.getElementById("studenti-container");
    container.innerHTML = "";

    data.forEach(student => {

        const card = document.createElement("div");

        card.innerHTML = `
            <h3>${student.name} ${student.surname}</h3>
            <p>${student.nickname}</p>
            <p>Vek: ${student.age}</p>
        `;

        card.style.border = "2px solid #ccc";
        card.style.padding = "10px";
        card.style.margin = "10px";
        card.style.cursor = "pointer";
        card.style.borderRadius = "10px";
        card.style.display = "inline-block";

        card.addEventListener("click", () => {

            selectedStudent = student;

            document.querySelectorAll("#studenti-container div")
                .forEach(el => el.style.background = "white");

            card.style.background = "#d0ebff";
        });

        container.appendChild(card);
    });
}


// =========================
// SORT SELECT
// =========================

document.addEventListener("DOMContentLoaded", () => {

    loadStudents();

    const select = document.getElementById("sortSelect");

    if (select) {
        select.addEventListener("change", (e) => {
            loadStudents(e.target.value);
        });
    }
});


// =========================
// CHAT
// =========================

async function sendMessage() {

    const input = document.getElementById("chat-input");
    const chatBox = document.getElementById("chat-box");

    const text = input.value.trim();
    if (!text) return;

    chatBox.innerHTML += `<div><b>Ty:</b> ${text}</div>`;

    messages.push({ role: "user", content: text });

    input.value = "";

    const res = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            messages,
            student: selectedStudent
        })
    });

    const data = await res.json();

    chatBox.innerHTML += `<div><b>AI:</b> ${data.reply}</div>`;

    messages.push({ role: "assistant", content: data.reply });
}
