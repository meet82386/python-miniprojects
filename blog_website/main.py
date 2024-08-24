from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    number = randint(1, 200)
    current_year = datetime.now().year
    return render_template("index.html", num=number, curr_year=current_year)


@app.route("/guess/<name>")
def guess_age(name):
    age = requests.get(f"https://api.agify.io/?name={name}").json()['age']
    gender = requests.get(f"https://api.genderize.io/?name={name}").json()['gender']
    return render_template("guess_age.html", name=name, age=age, gender=gender)


@app.route("/blog/<id>")
def get_blog(id):
    data = requests.get("https://api.npoint.io/75b10cfd1e9cd48d97b7").json()
    return render_template("blog.html", data=data, id=int(id))


if __name__ == "__main__":
    app.run(debug=True)