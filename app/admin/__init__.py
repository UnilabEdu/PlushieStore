from flask_admin import Admin
from app.admin.base import CustomAdminIndexView, SecureModelView

admin = Admin(name="Plushie Store", index_view=CustomAdminIndexView())