from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, URL

class Entry_Form(FlaskForm):
    name = StringField('name', validators=[DataRequired()]))
    email = StringField('email', validators=[DataRequired()]))
    password = PasswordField('password', validators=[DataRequired()]))
    title = StringField("Blog Post Title", validators=[DataRequired()])
    imestamp = DateTimeLocalField("When did this happen?", format="%Y-%m-%dT%H:%M", validators=[DataRequired()])
    trigger = StringField("What do you think the trigger is?", validators=[DataRequired()])
    reset_info = StringField("What's the current time of the day?", validators=[DataRequired()])
    submit = SubmitField("Submit")
