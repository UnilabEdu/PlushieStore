const navBurger = document.querySelector(".burger");
const navLinks = document.querySelector(".nav-links");

function navActiveToggler() {
    navLinks.classList.toggle("nav-links__active");
}

navBurger.addEventListener("click", navActiveToggler);

let btn1 = document.getElementById('buyButton')
var counters = document.querySelectorAll(".counter");

document.querySelector(".counter").innerHTML = localStorage.getItem("Quantity");

var amount = document.querySelector(".counter").innerHTML;
var addHref = document.getElementById("cartIcon")

if (amount !== '0') {
  addHref.href = "app/templates/product/cart.html"
}





















