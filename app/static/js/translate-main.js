var dataReload = document.querySelectorAll("[data-reload")

var findlink = document.getElementById("logoLink")
var addhash1 = document.getElementById("firstCategory")
var addhash2 = document.getElementById("secondCategory")
var HashFeatured1 = document.getElementById("featuredToy1")
var HashFeatured2 = document.getElementById("featuredToy2")
var HashFeatured3 = document.getElementById("featuredToy3")
var HashFeatured4 = document.getElementById("featuredToy4")
var HashFeatured5 = document.getElementById("featuredToy5")
var HashFeatured6 = document.getElementById("featuredToy6")
var HashFeatured7 = document.getElementById("featuredToy7")
var HashBasketButton1 = document.getElementById("bunnyButton")
var HashBasketButton2 = document.getElementById("animalButton")


var language = {
    eng: {
        FirstTab: "Popular",
        SecondTab: "Delivery Service",
        ThirdTab: "Contact",
        additionalTab: "Questions",
        conditionsTab: "Terms and Conditions",
        button: "Buy",
        bunnies: "Bunnies",
        animals: "Animals",
        popular: "Popular Toys",
        tbilisi: "We are delivering in Tbilisi on a second day from ordering. Delivery price in central parts of city is 6Gel and in outskirts - 8Gel.",
        regions: "We are sending toys in regions by post. Delivery price for towns is 10Gel and for villages 12Gel. The time of delivery depends on the address.",
        basket: "Basket is empty",
        basketButton1: "Choose bunny",
        basketButton2: "Choose other animal"
    }
};

if (window.location.hash) {
    if (window.location.hash === "#eng") {
        featuredProducts.textContent = language.eng.FirstTab;
        deliveryTab.textContent = language.eng.SecondTab;
        contactTab.textContent = language.eng.ThirdTab;
        questionsTab.textContent = language.eng.additionalTab;
        termsTab.textContent = language.eng.conditionsTab;
        buyButton1.textContent = language.eng.button;
        buyButton2.textContent = language.eng.button;
        buyButton3.textContent = language.eng.button;
        buyButton4.textContent = language.eng.button;
        buyButton5.textContent = language.eng.button;
        buyButton6.textContent = language.eng.button;
        buyButton7.textContent = language.eng.button;
        categoryBunnies.textContent = language.eng.bunnies;
        categoryAnimals.textContent = language.eng.animals;
        popularToys.textContent = language.eng.popular;
        deliverySectionTitle.textContent = language.eng.SecondTab;
        deliveryTbilisi.textContent = language.eng.tbilisi;
        deliveryRegions.textContent = language.eng.regions;
        burgerBunnies.textContent = language.eng.bunnies;
        burgerAnimals.textContent = language.eng.animals;
        burgerDelivery.textContent = language.eng.SecondTab;
        burgerContact.textContent = language.eng.ThirdTab;
        burgerQuestions.textContent = language.eng.additionalTab;
        emptyCart.textContent = language.eng.basket;
        bunnyButton.textContent = language.eng.basketButton1;
        animalButton.textContent = language.eng.basketButton2;

        const myfont = document.querySelectorAll("#phone, #mail, #termsTab, #animalButton, #bunnyButton, #emptyCart, #burgerQuestions, #burgerContact, #burgerDelivery, #burgerAnimals, #burgerBunnies, #featuredProducts, #questionsTab, #deliveryTab, #contactTab, #buyButton1, #buyButton2, #buyButton3, #buyButton4, #buyButton5, #buyButton6, #buyButton7, #categoryBunnies, #categoryAnimals, #popularToys, #deliverySectionTitle, #deliveryTbilisi, #deliveryRegions, #contactSectionTitle");

        myfont.forEach((element) => {
            element.style.fontFamily = "Handlee";
        });

            findlink.href = "#eng";
            addhash1.href = "app/templates/product/bunnies.html#eng"
            addhash2.href = "app/templates/product/bunnies.html#eng"
            HashFeatured1.href = "app/templates/product/product-page.html#eng"
            HashFeatured2.href = "app/templates/product/product-page.html#eng"
            HashFeatured3.href = "app/templates/product/product-page.html#eng"
            HashFeatured4.href = "app/templates/product/product-page.html#eng"
            HashFeatured5.href = "app/templates/product/product-page.html#eng"
            HashFeatured6.href = "app/templates/product/product-page.html#eng"
            HashFeatured7.href = "app/templates/product/product-page.html#eng"
            HashBasketButton1.href = "app/templates/product/bunnies.html#eng"
            HashBasketButton2.href = "app/templates/product/bunnies.html#eng"
    }
}

function PageReload() {
    setTimeout(function () {
      location.reload();
    }, 100);
  }