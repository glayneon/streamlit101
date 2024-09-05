from flask import Flask, render_template, request, redirect, send_file
from berlinjob import BerlinJobs
from web3career import Web3
from wework import Wework
import tocsv as csv

db = {}
jobsearching = [Web3, Wework, BerlinJobs]

app = Flask("Job Searching on Job Markets")

@app.route("/")
def home():
    return render_template("home.html", name='Search')

@app.route('/hello')
def hello():
    return 'hello you!'

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    if keyword is not None:
        if keyword in db:
            jobs = db[keyword]
        else:
            jobs = []
            for i in jobsearching:
                r = i()
                r.scrap_jobs(keyword)
                jobs += r.job_data
            db[keyword] = jobs
    else:
        return redirect('/')

    return render_template('search.html', keyword=keyword, jobs=jobs)

@app.route('/export')
def export():
    keyword = request.args.get('keyword')
    if keyword is None:
        return redirect('/')
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    
    filename = csv.save_to_csv(keyword, db[keyword])
    return send_file(filename, as_attachment=True)

app.run("0.0.0.0", debug=True)