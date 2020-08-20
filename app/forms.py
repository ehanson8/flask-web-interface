from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class EntryForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()],
                      default='https://dataverse.harvard.edu/oai')
    format = StringField('Format', validators=[DataRequired()],
                         default='oai_dc')
    set = StringField('Set', validators=[DataRequired()],
                      default='Jameel_Poverty_Action_Lab')
    submit = SubmitField('Submit')
