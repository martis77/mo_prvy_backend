fetch("http://127.0.0.1:5000/api")
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById("studenti-container");
        
        data.forEach(student => {
            const card = document.createElement("div");
            card.className = "student-card";
            
            card.innerHTML = `
                <img src="${student.image}" width="100">
                <h3>${student.name} ${student.surname}</h3>
                <p><b>${student.nickname}</b></p>
            `;
            container.appendChild(card);
        });
    })
    .catch(error => console.error("Chyba: Nezabudol si zapnúť Flask v termináli?", error));
