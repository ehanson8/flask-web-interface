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
        session['field'] = rec_form.field.data
        session['values_or_count'] = rec_form.values_or_count.data
        flash(
              'Submitted URL: {}, Repository: {}, Record Type: {}, '
              'Field: {}, Values or Count: {}'.format(
                                rec_form.url.data, rec_form.repo_id.data,
                                rec_form.rec_type.data, rec_form.field.data,
                                rec_form.values_or_count.data
              )
        )
        return redirect(url_for('report'))
    return render_template('record.html', title='Record Report', form=rec_form)


@app.route('/report')
def report():
    if 'search' in session:
        dict_list = models.search_report(
                                      session['url'],
                                      session['repo_id'],
                                      session['rec_type'],
                                      session['field'],
                                      session['search']
        )
    else:
        dict_list = models.rec_report(
                                      session['url'],
                                      session['repo_id'],
                                      session['rec_type'],
                                      session['field'],
                                      session['values_or_count']
        )
    return render_template(
        'report.html', title='Report Results', dict_list=dict_list
    )
