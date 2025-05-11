document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".btn-mostrar").forEach(button => {
        button.addEventListener("click", function() {
            let reverso = this.previousElementSibling;
            if (reverso.classList.contains("oculto")) {
                reverso.style.display = "block";
                reverso.classList.remove("oculto");
                this.textContent = "Ocultar Respuesta";
            } else {
                reverso.style.display = "none";
                reverso.classList.add("oculto");
                this.textContent = "Mostrar Respuesta";
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    let tarjetas = document.querySelectorAll(".tarjeta");
    let indiceActual = 0;

    function mostrarTarjeta(index) {
        tarjetas.forEach((tarjeta, i) => {
            tarjeta.style.display = i === index ? "block" : "none";
        });
    }

    document.querySelectorAll(".btn-anterior").forEach(button => {
        button.addEventListener("click", function() {
            if (indiceActual > 0) {
                indiceActual--;
                mostrarTarjeta(indiceActual);
            }
        });
    });

    document.querySelectorAll(".btn-siguiente").forEach(button => {
        button.addEventListener("click", function() {
            if (indiceActual < tarjetas.length - 1) {
                indiceActual++;
                mostrarTarjeta(indiceActual);
            }
        });
    });

    mostrarTarjeta(indiceActual);  // Mostrar la primera tarjeta al cargar la página
});
