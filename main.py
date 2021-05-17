from flask import Flask, render_template
from flask.templating import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/aboutme/')
def about():
    return render_template("aboutme.html")

@app.route('/portfolio/')
def portefolio():
    return render_template("portfolio.html")

@app.route("/portfolio/Fakebook/")
def fakebook():
    return render_template("Fakebook.html")

@app.route("/portfolio/Boogle/")
def boogle():
    return render_template("Boogle.html")


@app.route("/portfolio/hair salon/")
def hairsalon():
    return render_template("hair-salon.html")


if __name__ == '__main__':
    app.run(use_reloader=True)