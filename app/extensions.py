from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_babel import Babel


db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
ckeditor = CKEditor()
babel = Babel()
