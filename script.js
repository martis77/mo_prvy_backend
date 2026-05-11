const API_URL = "https://moj-prvy-backend-4.onrender.com";

let selectedStudent = null;
let messages = [];

// =========================
// ŠTUDENTI
// =========================

fetch(`${API_URL}/api`)
    .then(res => res.json())
    .then(data => {
        const container = document.getElementById("studenti-container");
        container.innerHTML = "";

        data.forEach(student => {
            const card = document.createElement("div");

            card.innerHTML = `
                <h3>${student.name} ${student.surname}</h3>
                <p>${student.nickname}</p>
            `;

            card.style.border = "2px solid #ccc";
            card.style.padding = "10px";
            card.style.margin = "10px";
            card.style.cursor = "pointer";
            card.style.borderRadius = "10px";
            card.style.display = "inline-block";

            // ⭐ DÔLEŽITÉ - klik musí byť tu
            card.addEventListener("click", () => {
                selectedStudent = student;

                console.log("Vybraný študent:", selectedStudent);

                document.querySelectorAll("#studenti-container div")
                    .forEach(el => el.style.background = "white");

                card.style.background = "#d0ebff";
            });

            container.appendChild(card);
        });
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

    try {
        const res = await fetch(`${API_URL}/chat`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                messages,
                student: selectedStudent
            })
        });

        const data = await res.json();

        console.log("Backend response:", data);

        chatBox.innerHTML += `<div><b>AI:</b> ${data.reply || "Žiadna odpoveď"}</div>`;
        messages.push({ role: "assistant", content: data.reply });

    } catch (err) {
        chatBox.innerHTML += `<div style="color:red;">Chyba servera</div>`;
        console.error(err);
    }
}
