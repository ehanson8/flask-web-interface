from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()],
                      default='https://aspace-staff-dev.mit.edu/staff/api')
    repo_id = RadioField('Repository', validators=[DataRequired()],
                         choices=['2', '5'],
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
                         choices=['2', '5'],
                         default='2')
    rec_type = RadioField('Record Type', validators=[DataRequired()],
                          choices=['accessions', 'resources'],
                          default='resources')
    field1 = StringField('Field 1', validators=[DataRequired()])
    values_or_count1 = RadioField('Values or Count for Field 1',
                                  validators=[DataRequired()],
                                  choices=['count', 'values'],
                                  default='values')
    field2 = StringField('Field 2 (Optional)')
    values_or_count2 = RadioField('Values or Count for Field 2',
                                  choices=['count', 'values'],
                                  default='values')
    submit = SubmitField('Submit')
