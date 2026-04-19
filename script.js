// =========================
// ŠTUDENTI (tvoje pôvodné)
// =========================
fetch("http://127.0.0.1:5000/api")
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

            card.innerHTML = `
                <img src="${student.image}" alt="${student.name}" 
                     style="width: 100px; height: 100px; border-radius: 50%; margin-bottom: 10px;">
                <h3>${student.name} ${student.surname}</h3>
                <p>Prezývka: <b>${student.nickname}</b></p>
            `;

            container.appendChild(card);
        });
    });


// =========================
// AI CHATBOT
// =========================

let messages = [];

async function sendMessage() {
    const input = document.getElementById("chat-input");
    const chatBox = document.getElementById("chat-box");

    const text = input.value.trim();
    if (!text) return;

    // zobraz user správu
    chatBox.innerHTML += `<div><b>Ty:</b> ${text}</div>`;

    messages.push({ role: "user", content: text });

    input.value = "";

    // loading efekt
    chatBox.innerHTML += `<div id="loading">AI píše...</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const res = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ messages })
        });

        const data = await res.json();

        // odstráni loading
        document.getElementById("loading").remove();

        // zobraz odpoveď
        chatBox.innerHTML += `<div><b>AI:</b> ${data.reply}</div>`;

        messages.push({ role: "assistant", content: data.reply });

        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (err) {
        document.getElementById("loading").remove();
        chatBox.innerHTML += `<div style="color:red;">Chyba: backend nebeží</div>`;
    }
}
