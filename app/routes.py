from flask import flash, redirect, render_template, session, url_for

from app import app, models
from app.forms import EntryForm


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = EntryForm()
    if form.validate_on_submit():
        session['url'] = form.url.data
        session['repo_id'] = form.repo_id.data
        session['rec_type'] = form.rec_type.data
        session['field'] = form.field.data
        flash(
              'Submitted URL: {}, Repository: {}, Record Type: {}, '
              'Field: {}'.format(
                                form.url.data, form.repo_id.data,
                                form.rec_type.data, form.field.data
              )
        )
        return redirect(url_for('report'))
    return render_template('index.html', title='Entry', form=form)


@app.route('/report')
def report():
    title_dict = models.create_dict_report(
                                            session['url'],
                                            session['repo_id'],
                                            session['rec_type'],
                                            session['field']
    )
    return render_template(
        'report.html', title='Report', title_dict=title_dict
    )
