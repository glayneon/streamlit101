from flask import Flask, render_template, request, redirect
from nagging import playtext

db = {}

app = Flask("Nagging to Children!!")

@app.route("/")
def home():
    return render_template("home.html", name='Search')

@app.route('/nagging')
def hello():
    keyword = request.args.get('keyword')
    if keyword is None:
        return redirect('/')
    else:
        playtext(keyword, 'ko')
        return render_template('nagging.html', keyword=keyword)

app.run("0.0.0.0", debug=True)