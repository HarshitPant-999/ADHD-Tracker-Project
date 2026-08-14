from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DateTimeLocalField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL, Optional

class EntryForm(FlaskForm):
    timestamp = DateTimeLocalField("When did this happen?", format="%Y-%m-%dT%H:%M", validators=[DataRequired()])
    trigger = TextAreaField("What do you think caused the crash", validators=[DataRequired()])
    sleep_time = IntegerField("Duration of today's sleep", validators=[DataRequired()])
    submit = SubmitField("Submit")

class ResolveForm(FlaskForm):
    reset_info = TextAreaField("How did it end?", validators=[DataRequired()])
    reset_time = IntegerField("How long it took to recover?", validators=[DataRequired()])
    submit = SubmitField("Submit")

class EditForm(FlaskForm):
    trigger = StringField("What do you think caused the crash", validators=[DataRequired()])
    reset_info = StringField("What helped you recover", validators=[Optional()])
    submit = SubmitField("Save Changes")
