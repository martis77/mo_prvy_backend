const API_URL = "https://moj-prvy-backend-4.onrender.com";

// =========================
// ŠTUDENTI
// =========================

let selectedStudent = null;

fetch(`${API_URL}/api`)
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById("studenti-container");
        container.innerHTML = "";

        data.forEach(student => {
            const card = document.createElement("div");

            card.style.border = "2px solid #ddd";
            card.style.borderRadius = "15px";
            card.style.padding = "15px";
            card.style.margin = "10px";
            card.style.display = "inline-block";
            card.style.textAlign = "center";
            card.style.width = "180px";
            card.style.boxShadow = "2px 2px 10px rgba(0,0,0,0.1)";
            card.style.cursor = "pointer";

            card.innerHTML = `
                <h3>${student.name} ${student.surname}</h3>
                <p>Prezývka: <b>${student.nickname}</b></p>
            `;

            // klik na študenta
            card.onclick = () => {
                selectedStudent = student;

                // highlight
                document.querySelectorAll(".selected").forEach(el => {
                    el.classList.remove("selected");
                    el.style.background = "white";
                });

                card.classList.add("selected");
                card.style.background = "#dff0ff";
            };

            container.appendChild(card);
        });
    });


// =========================
// CHAT
// =========================

let messages = [];

async function sendMessage() {
    const input = document.getElementById("chat-input");
    const chatBox = document.getElementById("chat-box");

    const text = input.value.trim();
    if (!text) return;

    chatBox.innerHTML += `<div><b>Ty:</b> ${text}</div>`;
    messages.push({ role: "user", content: text });

    input.value = "";

    chatBox.innerHTML += `<div id="loading">AI píše...</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const res = await fetch(`${API_URL}/chat`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                messages,
                student: selectedStudent
            })
        });

        const data = await res.json();

        document.getElementById("loading")?.remove();

        chatBox.innerHTML += `<div><b>AI:</b> ${data.reply ?? "Žiadna odpoveď"}</div>`;
        messages.push({ role: "assistant", content: data.reply });

        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (err) {
        document.getElementById("loading")?.remove();
        chatBox.innerHTML += `<div style="color:red;">Chyba: backend nebeží</div>`;
    }
}
