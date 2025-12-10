from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CRSFProtect()
csrf.init_app(app)

from application import routes


