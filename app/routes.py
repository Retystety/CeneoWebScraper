from app import app
from flask import render_template

@app.route('/')
@app.route('/index<name>')
def index(name = "HW"):
	text = "HW" 
	return render_template("index.html", text = text)

@app.route('/cos')
def cos():
	return "imię i nazwisko"