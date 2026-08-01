from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL

class EntryForm(FlaskForm):
    timestamp = DateTimeLocalField("When did this happen?", format="%Y-%m-%dT%H:%M", validators=[DataRequired()])
    trigger = TextAreaField("What do you think caused the crash", validators=[DataRequired()])
    reset_info = TextAreaField("How did it end?", validators=[DataRequired()])
    reset_time = IntegerField("How long it took recover?", validators=[DataRequired()])
    submit = SubmitField("Submit")

class ResolveForm(FlaskForm):
    reset_info = TextAreaField("How did it end?", validators=[DataRequired()])
    reset_time = IntegerField("How long it took to recover?", validators=[DataRequired()])
    submit = SubmitField("Submit")

