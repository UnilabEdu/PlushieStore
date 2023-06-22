import click
from flask.cli import with_appcontext
from app.extensions import db
from app.models import User, Role, ToyCategory, Order, Toy


@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Database Created")


@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Creating Product")

    # Roles
    roles = ['admin', 'member']
    for role in roles:
        new_role = Role(name=role)
        new_role.create()

    # Admin user
    admin_user = User(first_name="admin", last_name="", password='admin123', email="admin@gmail.com", phone="599999",
                      role_id=1)
    admin_user.create()

    # Toy Categorys
    toy_category1 = ToyCategory(name_geo="ბაჭიები", name_eng="bunny", description_geo="ბაჭიები",
                                description_eng="bunnys")
    toy_category2 = ToyCategory(name_geo="სხვა ცხოველები", name_eng="other animals", description_geo="სხვა ცხოველები",
                                description_eng="other animals")
    toy_category1.create(commit=False)
    toy_category2.create(commit=False)
    ToyCategory.save()

    # Toys
    for i in range(1, 7):
        toy1 = Toy(desc_eng=f"description {i}", desc_geo=f"აღწერა {i}", photo="", name_geo=f"ლურჯი ბაჭია {i}",
                   name_eng=f"blue bunny {i}", price=i + 30, stock=2,
                   is_popular=True, category_id=1)
        toy1.create(commit=False)
        toy2 = Toy(desc_eng=f"description {i}", desc_geo=f"აღწერა {i}", photo="", name_geo=f"ლურჯი ვეფხვი {i}",
                   name_eng=f"blue tiger {i}", price=i + 40, stock=2,
                   is_popular=False, category_id=2)
        toy2.create(commit=False)
    Toy.save()

    click.echo("Product Created")
