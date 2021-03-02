from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


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
    contact = TextAreaField('Contact',
                            validators=[DataRequired(),
                                        Length(max=5000,
                                               message="message cannot exceed %(max)d characters")])

    impressum = TextAreaField('Impressum',
                              validators=[DataRequired(),
                                          Length(max=500000,
                                                 message="message cannot exceed %(max)d characters")])
    submit = SubmitField('Submit')
