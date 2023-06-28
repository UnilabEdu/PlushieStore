var dataReload = document.querySelectorAll("[data-reload")

var findlink = document.getElementById("logoLink")
var addHash = document.getElementById("cartIcon")


var language = {
    eng: {
        FirstTab: "Popular",
        ThirdTab: "Contact",
        bunnies: "Bunnies",
        animals: "Animals",
        title: "Cart",
        price: "Price:",
        amount: "Quantity:",
        cartTotal: "Total:",
        delete: "remove",
        senderName: "Sender's full name",
        recipientName: "Recipient's full name",
        senderPhone: "Sender's phone number",
        recipientPhone: "Recipient's phone number",
        senderEmail: "Sender's email",
        recipientAddress: "Recipient's address",
        payment: "Pay"
    }
};

if (window.location.hash) {
    if (window.location.hash === "#eng") {
        burgerBunnies.textContent = language.eng.bunnies;
        burgerAnimals.textContent = language.eng.animals;
        burgerDelivery.textContent = language.eng.SecondTab;
        burgerContact.textContent = language.eng.ThirdTab;
        cartTitle.textContent = language.eng.title;
        cartPrice.textContent = language.eng.price;
        LSName.textContent = language.eng.senderName;
        LSPhone.textContent = language.eng.senderPhone;
        LSEmail.textContent = language.eng.senderEmail;
        LRName.textContent = language.eng.recipientName;
        LRPhone.textContent = language.eng.recipientPhone;
        LRAddress.textContent = language.eng.recipientAddress;
        cartPay.textContent = language.eng.payment;
        cartAmount.textContent = language.eng.amount;
        total.textContent = language.eng.cartTotal;
        remove.textContent = language.eng.delete

        const myfont = document.querySelectorAll("#remove, #total, #cartAmount, #cartPay, #LRAddress, #LRPhone, #LRName, #LSEmail, #LSPhone, #LSName, #adress, #rphone, #rname, #email, #phone, #sname, #cartPrice, #cartTitle, #burgerContact, #burgerDelivery, #burgerAnimals, #burgerBunnies");

        myfont.forEach((element) => {
            element.style.fontFamily = "Handlee";
        });

        findlink.href = "app/templates/product/cart.html#eng";
        addHash.href = "app/templates/product/cart.html#eng";
    }
}

function PageReload() {
    setTimeout(function () {
      location.reload();
    }, 100);
  }