from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField, RadioField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError


class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    description = TextAreaField("What's your pitch?", validators=[Required()])
    category = RadioField('Label', )
