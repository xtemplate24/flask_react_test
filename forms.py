from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class Todo(FlaskForm):
    content = TextAreaField(label="enter smth",validators=[DataRequired()])
    submit = SubmitField("Submit todo")