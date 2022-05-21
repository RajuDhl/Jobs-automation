import os
import time

from flask import Flask, render_template, request

from static.others.combine import combine_data
from static.others.filter import filter_data
from static.others.update_domain import update_domain
from flask import send_file
from static.others.text2csv import *
from static.others.utils import *

main = Flask(__name__)


@main.route('/')
def hello_world():
    return render_template('index.html')


@main.route('/<url>')
def redirect(url):
    path = request.path
    url = path[1:len(path)]
    file = f'{url}.html'
    print("url is", url)
    try:

        return render_template(file)
    except:
        pass
        return render_template('index.html', msg="URL does not exist")


@main.route('/text-csv', methods=['GET', 'POST'])
def text_to_csv():
    cwd = os.getcwd()
    if request.method == 'POST':
        site = request.form['site']
        logged_in = request.form['logged_in']
        path = save_file(request)  # save file in temp
        output = text2csv(path, site, logged_in)  # Convert to CSV
        # print(output)
        print(len(output))
        df = Dataframe(output, cwd)  # drop duplicates and append new data to processed jobs
        print('enriching df of size', len(df))
        out = enrich_domains(df, cwd)
        return send_file(out, as_attachment=True, attachment_filename='data.csv')


@main.route('/add-domain', methods=['GET', 'POST'])
def add_domain():
    print("Touched here")
    cwd = os.getcwd()
    if request.method == 'POST':
        path = save_file(request)
        out = enrich_domains(path, cwd)
        return send_file(out, as_attachment=True, attachment_filename='job file.csv')


@main.route('/download-sample/<filename>', methods=['GET', 'POST'])
def download_sample(filename):
    cwd = os.getcwd()
    path = f"{cwd}/data/static/samples/{filename}.csv"
    return send_file(path, as_attachment=True)


# Used to update domain for existing companies
@main.route('/update-domain', methods=['Get', 'Post'])
def update_company_domain():
    cwd = os.getcwd()
    if request.method == 'POST':
        path = save_file(request)
        output = update_domain(path, cwd)
        if output:
            return redirect('/')


@main.route('/filter-people', methods=['GET', 'POST'])
def filter_people():
    cwd = os.getcwd()
    if request.method == 'POST':
        path = save_file(request)
        output = filter_data(path, cwd)
        print("success")
        return send_file(output, as_attachment=True, attachment_filename='data.csv')


@main.route('/combine-final', methods=['GET', 'POST'])
def combine_final():
    print("joining final data")
    cwd = os.getcwd()
    if request.method == 'POST':
        path = save_file(request)
        output = combine_data(path, cwd)
        return send_file(output, as_attachment=True, attachment_filename='data.csv')


@main.route('/download/<path>', methods=['GET', 'POST'])
def download(path):
    print("hello world", path)
    return render_template('download.html')


@main.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files
        companies = files.getlist('companies')
        jobs = files.getlist('jobs')


@main.route('/uploader', methods=['GET', 'POST'])
def search_people():
    if request.method == 'POST':
        path = save_file(request)
        companies_path = path['companies']
        jobs_path = path['jobs']
        start = request.form['start']
        total = request.form['total']
        search = search_people_using_api(companies_path, jobs_path, start, total)

    else:
        print("Get request method")
    return render_template('download.html')
