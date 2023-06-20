import click
from flask.cli import with_appcontext
from app.extensions import db
from app.models import User, Role


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
    roles = ['admin', 'member']
    for role in roles:
        new_role = Role(name=role)
        new_role.create()

    admin_user = User(first_name="admin", last_name="", password='admin123', email="admin@gmail.com", phone="599999", role_id=1)
    admin_user.create()
    click.echo("Product Created")
