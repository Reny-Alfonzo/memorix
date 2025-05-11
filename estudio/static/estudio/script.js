document.addEventListener("DOMContentLoaded", function() {
    let tarjetas = document.querySelectorAll(".tarjeta");
    let indiceActual = 0;

    function mostrarTarjeta(index) {
        tarjetas.forEach((tarjeta, i) => {
            tarjeta.style.display = i === index ? "block" : "none";
        });
    }

    tarjetas.forEach(tarjeta => {
        tarjeta.addEventListener("click", function() {
            this.classList.toggle("flipped");
        });
    });

    document.querySelector(".flecha-izquierda").addEventListener("click", function() {
        if (indiceActual > 0) {
            indiceActual--;
            mostrarTarjeta(indiceActual);
        }
    });

    document.querySelector(".flecha-derecha").addEventListener("click", function() {
        if (indiceActual < tarjetas.length - 1) {
            indiceActual++;
            mostrarTarjeta(indiceActual);
        }
    });

    // ✅ MODO OSCURO - Alternar entre claro y oscuro
    function toggleModo() {
        document.body.classList.toggle("dark-mode");
        let btnModo = document.querySelector(".btn-modo");
        btnModo.textContent = document.body.classList.contains("dark-mode") ? "☀" : "🌙";
    }

    document.querySelector(".btn-modo").addEventListener("click", toggleModo);

    mostrarTarjeta(indiceActual);
});
