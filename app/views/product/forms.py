from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired


class CartForm(FlaskForm):
    ord_fullname = StringField("შემკვეთის სახელი და გვარი", validators=[DataRequired()])
    ord_phone = StringField("შემკვეთის ტელეფონი", validators=[DataRequired()])
    ord_email = EmailField("შემკვეთის ელ-ფოსტა", validators=[DataRequired()])

    fullname = StringField("მიმღების სახელი და გვარი", validators=[DataRequired()])
    phone = StringField("მიმღების ტელეფონი", validators=[DataRequired()])
    delivery_address = EmailField("მიმღების მისამართი", validators=[DataRequired()])

    submit = SubmitField("გადახდა")
