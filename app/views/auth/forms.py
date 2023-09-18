from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, EmailField, IntegerField, SubmitField
from wtforms.validators import DataRequired, equal_to, ValidationError
from app.models import User
from string import digits


class RegisterForm(FlaskForm):
    email = EmailField('ელფოსტა', validators=[DataRequired("შეიყვანე იმეილი")])
    phone_number = IntegerField('ტელეფონის ნომერი', validators=[DataRequired("შეიყვანე მობილური ნომერი")])
    fullname = StringField('სახელი და გვარი', validators=[DataRequired("შეიყვანე სახელი")])
    password = PasswordField('სასურველი პაროლი', validators=[DataRequired("შეიყვანე პაროლი")])
    confirm_password = PasswordField('გაიმეორეთ პაროლი', validators=[DataRequired("არ ემთხვევა პირვანდელს"),
                                                                     equal_to('password',
                                                                              message="პაროლი არ ემთხვევა")])

    submit = SubmitField('რეგისტრაცია')

    def validate_email(self, field):
        existing_email = User.query.filter_by(email=field.data).first()
        if existing_email:
            raise ValidationError("ელფოსტა უკვე გამოყენებულია")

    def validate_password(self, field):
        contains_digits = False
        for char in field.data:
            if char in digits:
                contains_digits = True

        if not contains_digits:
            raise ValidationError("პაროლი უნდა შეიცავდეს ციფრებს")

    def validate_fullname(self, field):
        fullname = field.data
        if len(fullname.split(" ", 1)) <= 1:
            raise ValidationError("შეიყვანეთ სახელი და გვარი სრულად")


class LoginForm(FlaskForm):
    email = EmailField('მომხმარებელი', validators=[DataRequired("შეიყვანეთ ელფოსტა")])
    password = PasswordField('პაროლი', validators=[DataRequired("შეიყვანეთ პაროლი")])
    submit = SubmitField('შესვლა')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if not user:
            raise ValidationError("ელფოსტა არასწორია, სცადეთ თავიდან")

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            if not user.check_password(field.data):
                raise ValidationError("პაროლი არასწორია, სცადეთ თავიდან")
