from flask_wtf import FlaskForm, widgets
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from app.models import Department


class DepartmentForm(FlaskForm):
    name = StringField('Department Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Department')

    def validate_name(self, field):
        if Department.query.filter_by(name=field.data).first():
            raise ValidationError('Department name: {} already exists'.format(field.data))
