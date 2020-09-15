from flask import flash, redirect, render_template, session, url_for

from app import app, models
from app.forms import RecordForm, SearchForm


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    search_form = SearchForm()
    if search_form.validate_on_submit():
        session.clear()
        session['url'] = search_form.url.data
        session['repo_id'] = search_form.repo_id.data
        session['rec_type'] = search_form.rec_type.data
        session['field'] = search_form.field.data
        session['search'] = search_form.search.data
        flash(
              'Submitted URL: {}, Repository: {}, Record Type: {}, '
              'Field: {}, Keyword: {}'.format(
                                search_form.url.data, search_form.repo_id.data,
                                search_form.rec_type.data,
                                search_form.field.data,
                                search_form.search.data
              )
        )
        return redirect(url_for('report'))
    return render_template('search.html', title='Search Report',
                           form=search_form)


@app.route('/record', methods=['GET', 'POST'])
def record():
    rec_form = RecordForm()
    if rec_form.validate_on_submit():
        session.clear()
        session['url'] = rec_form.url.data
        session['repo_id'] = rec_form.repo_id.data
        session['rec_type'] = rec_form.rec_type.data
        session['field1'] = rec_form.field1.data
        session['values_or_count1'] = rec_form.values_or_count1.data
        session['field2'] = rec_form.field2.data
        session['values_or_count2'] = rec_form.values_or_count2.data
        flash(
              'Submitted URL: {}, Repository: {}, Record Type: {}, '
              'Field 1: {}, Values or Count 1: {}, Field 2: {}, '
              'Values or Count 2: {}'.format(
                                rec_form.url.data, rec_form.repo_id.data,
                                rec_form.rec_type.data, rec_form.field1.data,
                                rec_form.values_or_count1.data,
                                rec_form.field2.data,
                                rec_form.values_or_count2.data
              )
        )
        return redirect(url_for('report'))
    return render_template('record.html', title='Record Report', form=rec_form)


@app.route('/report')
def report():
    if 'search' in session:
        file = models.search_report(
                                      session['url'],
                                      session['repo_id'],
                                      session['rec_type'],
                                      session['field'],
                                      session['search']
        )
    else:
        file = models.rec_report(
                                      session['url'],
                                      session['repo_id'],
                                      session['rec_type'],
                                      session['field1'],
                                      session['values_or_count1'],
                                      session['field2'],
                                      session['values_or_count2']
        )
    return render_template(
        'report.html', title='Report Results', file=file
    )
