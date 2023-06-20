from flask import Blueprint, render_template, flash, redirect, url_for, request
from os import path
from app.config import Config
from app.views.auth.forms import RegisterForm, LoginForm
from app.models import User
from flask_login import login_user, logout_user

TEMPLATE_FOLDER = path.join(Config.BASE_DIRECTORY, 'templates', 'auth')
auth_blueprint = Blueprint('auth', __name__, template_folder=TEMPLATE_FOLDER)


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        user.role_id = 2
        user.create()
        login_user(user)

        return redirect(url_for("main.home"))

    return render_template("register.html", form=form)


@auth_blueprint.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash("მომხმარებელი ვერ მოიძებნა")
            return redirect(url_for("auth.login"))

        if user.check_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if next:
                return redirect(next)
            elif user.role_id == 1:
                return redirect(url_for('admin.index'))
            else:
                return redirect(url_for("main.home"))
        else:
            flash("პაროლი არასწორია")
    return render_template("login.html", form=form)


@auth_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

