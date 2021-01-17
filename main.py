from flask import Flask
from flask_hcaptcha import hCaptcha
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown

from config import config
from document import DocumentManager

app = Flask(__name__)
app.config.from_mapping(config)

hcaptcha = hCaptcha(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
md = Markdown(app, output_format='html4')

document_manager = DocumentManager(app, "documents/documents.json")
