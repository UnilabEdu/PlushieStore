from flask import Blueprint, redirect, render_template, url_for
from app.config import Config
from os import path

TEMPALTE_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "product")
product_blueprint = Blueprint("product", __name__, template_folder=TEMPALTE_FOLDER)


@product_blueprint.route("/bunnies")
def bunnies():
    return render_template("bunnies.html")


@product_blueprint.route("/product")
def view_product():
    return render_template("product-page.html")


@product_blueprint.route("/other")
def other_animals():
    return render_template("other-animals.html")


@product_blueprint.route("/cart")
def cart():
    return render_template("cart.html")
