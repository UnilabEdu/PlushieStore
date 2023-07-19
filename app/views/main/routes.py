from flask import Blueprint, render_template, session, redirect, request
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


@main_blueprint.route("/terms")
def terms():
    return render_template("terms.html")


@main_blueprint.route("/questions")
def questions():
    return render_template("questions.html")


@main_blueprint.route("/change_ln")
def change_language():
    if session['locale'] == 'EN':
        session['locale'] = 'KA'
    else:
        session['locale'] = 'EN'

    previous_url = request.referrer
    return redirect(previous_url)
