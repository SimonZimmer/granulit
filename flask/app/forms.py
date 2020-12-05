from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class BioUpdateForm(FlaskForm):
    text = StringField('New text', validators=[DataRequired(), Length(max=300, message="message cannot exceed %(max)d characters")])
    submit = SubmitField('Update Bio')

