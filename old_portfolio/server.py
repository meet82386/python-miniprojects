from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/index2.html")
def index2():
    return render_template("index2.html")

@app.route("/contect.html")
def contect():
    return render_template("contect.html")


@app.route("/Hobbies.html")
def hobbies():
    return render_template("Hobbies.html")


if __name__ == "__main__":
    app.run(debug=True)
