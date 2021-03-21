from flask import Flask

from flaskext.mail import Mail,Message 
from .config import Config
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
csrf = CSRFProtect(app)

from app import views