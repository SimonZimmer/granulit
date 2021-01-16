from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class ContentUpdateForm(FlaskForm):
    bio = TextAreaField('Biography Text',
                         validators=[DataRequired(),
                                     Length(max=3000,
                                     message="message cannot exceed %(max)d characters")])
    releases = TextAreaField('Releases Embedded Links',
                         validators=[DataRequired(),
                                     Length(max=30000,
                                     message="message cannot exceed %(max)d characters")])
    podcasts = TextAreaField('Podcasts Embedded Links',
                         validators=[DataRequired(),
                                     Length(max=30000,
                                     message="message cannot exceed %(max)d characters")])
    videos = TextAreaField('Video Embedded Links',
                         validators=[DataRequired(),
                                     Length(max=30000,
                                     message="message cannot exceed %(max)d characters")])
    submit = SubmitField('Submit')

