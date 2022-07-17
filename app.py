from operator import truediv
from flask import Flask, render_template
import random
count = 0
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/games")
def games():
    return render_template('games.html')

@app.route("/writing")
def writing():
    return render_template('writing.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/ppt")
def ppt():
    return render_template('ppt.html')

@app.route("/other")
def other():
    return render_template('other.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

if __name__ == "__main__":
    app.run(debug=True)
