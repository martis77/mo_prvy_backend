// 1. Zavoláme náš Flask backend
fetch("http://127.0.0.1:5000/api")
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById("studenti-container");
        container.innerHTML = ""; // Vyčistíme text "Načítavam..."

        // 2. Prejdeme každého študenta zo zoznamu
        data.forEach(student => {
            const card = document.createElement("div");
            
            // Štýl pre kartičku
            card.style.border = "2px solid #ddd";
            card.style.borderRadius = "15px";
            card.style.padding = "15px";
            card.style.margin = "10px";
            card.style.display = "inline-block";
            card.style.textAlign = "center";
            card.style.width = "180px";
            card.style.boxShadow = "2px 2px 10px rgba(0,0,0,0.1)";

            // 3. VLOŽENIE OBRÁZKA (Skontroluj, či sa v Pythone volá "image")
            card.innerHTML = `
                <img src="${student.image}" alt="${student.name}" 
                     style="width: 100px; height: 100px; border-radius: 50%; background: #f0f0f0; margin-bottom: 10px;">
                <h3 style="margin: 5px 0;">${student.name} ${student.surname}</h3>
                <p style="color: #666;">Preývka: <b>${student.nickname}</b></p>
            `;
            
            container.appendChild(card);
        });
    })
    .catch(error => {
        console.error("Chyba:", error);
        document.getElementById("studenti-container").innerHTML = 
            "<p style='color:red;'>Chyba: Nezabudni spustiť Python (py app.py)!</p>";
    });
