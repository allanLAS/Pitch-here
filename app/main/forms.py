from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField, RadioField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError


class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    description = TextAreaField("What's your pitch?", validators=[Required()])
    category = RadioField('Label', choices=[('promotionpitch','promotionpitch'),('interviewpitch', 'interviewpitch'),('pickuplines','pickuplines'),('productpitch','productpitch')], validators=[Required()])
    submit = SubmitField('submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Add a comment..')
    submit = SubmitField('Submit')


class UpvoteForm(FlaskForm):
    submit = SubmitField()


class DownvoteForm(FlaskForm):
    submit = SubmitField()

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

