from app import app
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index/<name>')
def index(name="<<Hello World>>"):
    return render_template("index.html.jinja", text=name)

@app.route('/extract')
def extract():
    import scraper
    import analyzer
    pass


@app.route('products')
def products():
    return render_template("product.html.jinja")

@app.route('/author')
def author():
    return render_template("author.html.jinja")

@app.route('/product/<product_id>')
def product():
    pass
