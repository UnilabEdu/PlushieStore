from flask import Blueprint, redirect, render_template, url_for
from app.config import Config
from os import path
from app.models import ToyCategory, Toy

TEMPALTE_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPALTE_FOLDER)


@main_blueprint.route("/")
def home():
    toys = Toy.query.filter_by(is_popular=True)[:7]
    categories = ToyCategory.query.all()
    return render_template("index.html", categories=categories, toys=toys)
