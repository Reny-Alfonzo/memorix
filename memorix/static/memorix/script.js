document.addEventListener("DOMContentLoaded", function() {
    const burger = document.querySelector(".navbar-burger");
    const navMenu = document.querySelector("#navMenu");

    burger.addEventListener("click", function() {
        burger.classList.toggle("is-active");
        navMenu.classList.toggle("is-active");
    });
});
