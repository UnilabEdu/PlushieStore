from flask_admin import Admin
from app.admin.base import CustomAdminIndexView, SecureModelView
from app.admin.user import UserView
from app.admin.store import CityView, OrderView, ToyView, ToyCategoryView


admin = Admin(name="Plushie Store", index_view=CustomAdminIndexView())
