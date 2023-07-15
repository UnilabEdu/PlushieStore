from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, EmailField, IntegerField, SubmitField, RadioField
from wtforms.validators import DataRequired, equal_to, ValidationError
from app.models import User
from string import digits


class RegisterForm(FlaskForm):
    first_name = StringField('სახელი', validators=[DataRequired("შეიყვანე სახელი")])
    last_name = StringField('გვარი', validators=[DataRequired("შეიყვანე გვარი")])
    password = PasswordField('პაროლი', validators=[DataRequired("შეიყვანე პაროლი")])
    confirm_password = PasswordField('დაადასტურე პაროლი', validators=[DataRequired("არ ემთხვევა პირვანდელს"),
                                                                      equal_to('password',
                                                                               message="პაროლი არ ემთხვევა")])
    email = EmailField('იმელი', validators=[DataRequired("შეიყვანე იმეილი")])
    phone_number = IntegerField('ტელეფონის ნომერი', validators=[DataRequired("შეიყვანე მობილური ნომერი")])

    submit = SubmitField('რეგისტრაცია')

    def validate_email(self, field):
        existing_email = User.query.filter_by(email=field.data).first()
        if existing_email:
            raise ValidationError("იმეილი უკვე გამოყენებულია")

    def validate_password(self, field):
        contains_digits = False
        for char in field.data:
            if char in digits:
                contains_digits = True

        if not contains_digits:
            raise ValidationError("პაროლი უნდა შეიცავდეს ციფრებს")


class LoginForm(FlaskForm):
    email = EmailField('მომხმარებელი', validators=[DataRequired("შეიყვანეთ მეილი")])
    password = PasswordField('პაროლი', validators=[DataRequired("შეიყვანეთ პაროლი")])
    submit = SubmitField('შესვლა')
