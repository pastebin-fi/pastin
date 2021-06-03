from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, BooleanField
from wtforms.validators import ValidationError, DataRequired

from flask import flash
from main import db

class PasteForm(FlaskForm):
    # TODO: Localize error messages
    name = StringField(validators=[DataRequired(message= \
        "Pastella tulee olla nimi.")])
    content = TextAreaField(validators=[DataRequired(message= \
        "Tyhjää pastea ei voida luoda.")])
    private = BooleanField()

class Paste(db.Model):
    id = db.Column(db.String(16), primary_key=True)
    content = db.Column(db.UnicodeText)
    # TODO: Localize default name
    name = db.Column(db.String(1048576), default="Nimetön paste")
    private = db.Column(db.Boolean, default=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def defaults(self):
        if not self.name:
            self.name = "Nimetön paste"
