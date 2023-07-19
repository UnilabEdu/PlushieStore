from flask import Blueprint, render_template, flash, redirect, url_for, request
from os import path
from app.config import Config
from app.views.auth.forms import RegisterForm, LoginForm
from app.models import User
from flask_login import login_user, logout_user, current_user

TEMPLATE_FOLDER = path.join(Config.BASE_DIRECTORY, 'templates', 'auth')
auth_blueprint = Blueprint('auth', __name__, template_folder=TEMPLATE_FOLDER)


@auth_blueprint.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        fullname = form.fullname.data.split(" ", 1)
        user = User(first_name=fullname[0],
                    last_name=fullname[1],
                    password=form.password.data,
                    email=form.email.data,
                    phone=form.phone_number.data,
                    role_id=2
                    )
        user.create()
        login_user(user)

        return redirect(url_for("main.home"))
    else:
        error_msg = {}
        for tag, error in form.errors.items():
            error_msg[tag] = error[0]

    return render_template("register.html", form=form, error_msg=error_msg)


@auth_blueprint.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user)
        next = request.args.get('next')
        if next:
            return redirect(next)
        elif user.role_id == 1:
            return redirect('/admin/order/')
        else:
            return redirect(url_for("main.home"))
    else:
        error_msg = {}
        for tag, error in form.errors.items():
            error_msg[tag] = error[0]

    return render_template("login.html", form=form, error_msg=error_msg)


@auth_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth_blueprint.route("/reset-password", methods=['POST', 'GET'])
def reset_password():
    if request.method == "POST":
        user = User.query.get(current_user.id)

    return render_template("reset-password.html")
