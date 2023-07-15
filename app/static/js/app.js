const navBurger = document.querySelector(".burger");
const navLinks = document.querySelector(".nav-links");

function navActiveToggler() {
    navLinks.classList.toggle("nav-links__active");
}

navBurger.addEventListener("click", navActiveToggler);