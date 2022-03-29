from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)
app.secret_key = '1235;lkjqs;poiqfqsfjgag'

@app.route("/")

def index():
    if 'logged_in' in session:
        redirect(dashboard)
    return render_template("index.html")
