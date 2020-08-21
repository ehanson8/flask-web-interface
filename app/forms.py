from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class EntryForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()],
                      default='https://aspace-staff-dev.mit.edu/staff/api')
    repo_id = StringField('Repository', validators=[DataRequired()],
                          default='2')
    rec_type = SelectField('Record Type', validators=[DataRequired()],
                           choices=['accessions', 'resources'],
                           default='resources')
    field = StringField('Field', validators=[DataRequired()],
                        default='title')
    submit = SubmitField('Submit')
