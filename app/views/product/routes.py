from flask import Blueprint, render_template
from app.config import Config
from os import path
from app.models import Toy, ToyCategory

TEMPALTE_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "product")
product_blueprint = Blueprint("product", __name__, template_folder=TEMPALTE_FOLDER)


@product_blueprint.route("/categories/<int:category_id>")
def category(category_id):
    categorie = ToyCategory.query.get(category_id)
    toys = Toy.query.filter_by(category_id=categorie.id)
    return render_template("bunnies.html", toys=toys, categorie=categorie)


@product_blueprint.route("/product/<int:id>")
def view_product(id):
    toy = Toy.query.filter_by(id=id).first()
    return render_template("product-page.html", toy=toy)
