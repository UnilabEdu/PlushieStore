const navBurger = document.querySelector(".burger");
const navLinks = document.querySelector(".nav-links");

function navActiveToggler() {
    navLinks.classList.toggle("nav-links__active");
}

navBurger.addEventListener("click", navActiveToggler);

let btn1 = document.getElementById('buyButton')
var counters = document.querySelectorAll(".counter");
var addHref = document.getElementById("cartIcon");

if (btn1 !== null) {
  btn1.addEventListener("click", btn1Count);
  function btn1Count () {
    counters[0].textContent = parseInt(counters[0].textContent) + 1;
    var spanText = document.querySelector(".counter-active").innerHTML;
    localStorage.setItem("Quantity",spanText)
    location.reload()
  }
}

document.querySelector(".counter").innerHTML = localStorage.getItem("Quantity");

var amount = document.querySelector(".counter-active").innerHTML;

if (amount !== '0') {
  document.getElementById('myModal').remove();
  if (window.location.hash === "#eng") {
    addHref.href = "../product/cart.html#eng";
  }
  else {
    addHref.href = "../product/cart.html";
  }
}

























