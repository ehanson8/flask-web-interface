from flask import flash, redirect, render_template, session, url_for

from app import app, models
from app.forms import EntryForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/entry', methods=['GET', 'POST'])
def entry():
    form = EntryForm()
    if form.validate_on_submit():
        session['url'] = form.url.data
        session['format'] = form.format.data
        session['set'] = form.set.data
        flash('Submitted URL: {}, Set: {}, Format: {}'.format(
            form.url.data, form.set.data, form.format.data))
        return redirect(url_for('report'))
    return render_template('entry.html', title='Entry', form=form)


@app.route('/report')
def report():
    field = 'title'
    title_dict = models.create_dict_report(session['url'], session['format'],
                                           session['set'], field)
    return render_template(
        'report.html', title='Report', title_dict=title_dict
    )
