from tkinter import *
import pandas as pd
from random import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
current_word = {}
to_learn = {}

try:
    data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/french_words.csv')
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=front_image)
    current_word = choice(to_learn)
    canvas.itemconfig(language_name, text="French", fill='black')
    canvas.itemconfig(content, text=current_word["French"], fill='black')
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(language_name, text="English", fill='white')
    canvas.itemconfig(content, text=current_word["English"], fill='white')


def is_known():
    to_learn.remove(current_word)
    updated_data = pd.DataFrame(to_learn)
    updated_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash Cards")
window.minsize(width=500, height=500)
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)

# Buttons
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
language_name = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
content = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=next_card)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=flip_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
