from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()],
                      default='https://aspace-staff-dev.mit.edu/staff/api')
    repo_id = RadioField('Repository', validators=[DataRequired()],
                         choices=['2', '3', '4', '5', '6', '7', '8', '9',
                                  '10'],
                         default='2')
    rec_type = RadioField('Record Type', validators=[DataRequired()],
                          choices=['accession', 'resource'],
                          default='resource')
    field = StringField('Field', validators=[DataRequired()],
                        default='keyword')
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RecordForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()],
                      default='https://aspace-staff-dev.mit.edu/staff/api')
    repo_id = RadioField('Repository', validators=[DataRequired()],
                         choices=['2', '3', '4', '5', '6', '7', '8', '9',
                                  '10'],
                         default='2')
    rec_type = RadioField('Record Type', validators=[DataRequired()],
                          choices=['accessions', 'resources'],
                          default='resources')
    field = StringField('Field', validators=[DataRequired()])
    values_or_count = RadioField('Values or Count',
                                 validators=[DataRequired()],
                                 choices=['count', 'values'],
                                 default='values')
    submit = SubmitField('Submit')
