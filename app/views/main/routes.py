from flask import Blueprint, redirect, render_template, url_for
from app.config import Config
from os import path

TEMPALTE_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")
main_blueprint = Blueprint("main", __name__, template_folder=TEMPALTE_FOLDER)


@main_blueprint.route("/")
def home():
    return render_template("index.html")

