from flask import Flask
from random import randint

app = Flask(__name__)
number = randint(0,9)


@app.route("/")
def home():
    return '<h1>Guess the number between 0 and 9</h1>' \
        '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnBndXN5dGs1aW5jcTBweTFleWx4aWdqdXZiYmRmbjRncWk0aGV0YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WRQBXSCnEFJIuxktnw/giphy.gif" width=200>'


@app.route("/<int:n>")
def check_number(n):
    print(number)
    if n < number:
        return '<h1>Too low, Try higher number.</h1>' \
        '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXdhdG1wcDE2MHY3NmVtdTN1a2VvZ3VubGloZ2E5ajVuMWlvNXN4ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OjiSLBg7s27kaIGS8o/giphy.gif" width=200>'

    elif n > number:
        return '<h1>Too high, Try lower number.</h1>' \
        '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXdhdG1wcDE2MHY3NmVtdTN1a2VvZ3VubGloZ2E5ajVuMWlvNXN4ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OjiSLBg7s27kaIGS8o/giphy.gif" width=200>'

    else:
        return '<h1>Yay, you found the number.</h1>' \
        '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDh3eWlsOW02bmFoZXdrbmlmc3M0bW44cjc4MGlxOTN1czZvYWFvZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1DTBGm5Rfgymk/giphy.gif" width=200>'


if __name__ == "__main__":
    app.run(debug=True)
    