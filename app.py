from flask import Flask, url_for, render_template


app = Flask("__name__")

@app.route("/")
def home():
    return render_template("/templates/index.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("/templates/quemsomos.html")

@app.route("/contato")
def contato():
    return render_template("/templates/contato.html")