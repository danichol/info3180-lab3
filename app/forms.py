from flask_wtf import FlaskForm

from wtforms import TextField,TextAreaField, SubmitField
from wtforms.validators import DataRequired,Email

class ContactForm(FlaskForm):
    name = TextField('name', validators=[DataRequired()]))
    email = TextField('email', validators=[DataRequired(),Email()])
    subject = TextField('subject', validators[DataRequired()])
    body = TextAreaField('textarea',validators[DataRequired()])
    
    