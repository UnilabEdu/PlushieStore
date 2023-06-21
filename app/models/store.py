from app.models import BaseModel
from app.extensions import db


class City(db.Model, BaseModel):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    name_geo = db.Column(db.String, nullable=False)
    name_eng = db.Column(db.String, nullable=False)
    delivery_cost = db.Column(db.Float, nullable=False)
    delivery_delay = db.Column(db.Integer, nullable=False)


class Toy(db.Model, BaseModel):
    __tablename__ = "toys"

    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String, nullable=False)
    name_geo = db.Column(db.String, nullable=False)
    name_eng = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    is_popular = db.Column(db.Boolean)
    category_id = db.ForeignKey("toy_categories.id")


class ToyCategory(db.Model, BaseModel):
    __tablename__ = "toy_categories"

    id = db.Column(db.Integer, primary_key=True)
    name_geo = db.Column(db.String, nullable=False)
    name_eng = db.Column(db.String, nullable=False)
    description_geo = db.Column(db.String, nullable=False)
    description_eng = db.Column(db.String, nullable=False)


class Order(db.Model, BaseModel):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String)
    ordered_toys = db.Column(db.String)
    order_price = db.Column(db.Float)
    customer_info = db.Column(db.String)
    customer_phone = db.Column(db.String)
    customer_address = db.Column(db.String)
    customer_note = db.Column(db.String)
    order_status = db.Column(db.String)
    order_date = db.Column(db.String)
    delivery_date = db.Column(db.String)
    admin_note = db.Column(db.String)

