import json
from importlib.metadata import entry_points
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = "qwertyuioplkjhgfdsazxcvbnmMNBVCXZASDFGHJKLPOIUYTREWQ"
    numbers = "1234567890"
    specials = "!@#$%^&*()"

    password = [choice(letters) for _ in range(randint(8, 10))]
    password.extend([choice(numbers) for _ in range(randint(2, 4))])
    password.extend([choice(specials) for _ in range(randint(2, 4))])

    shuffle(password)
    password = "".join(password)
    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SEARCH CREDENTIALS ------------------------------- #
def search_password():
    entry_value = website_entry.get()

    with open("data.json") as file:
        data = json.load(file)
        try:
            data_dict = data[entry_value]
            messagebox.showinfo(title=entry_value, message=f"email: {data_dict['email']}\n"
                                                       f"password: {data_dict['password']}\n")
        except (KeyError, FileNotFoundError):
            messagebox.showinfo(title="Not Found", message="Credentials not found!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if website == "":
        messagebox.showinfo(title="Missing Field", message="Site name is empty.")
        return

    if email == "":
        messagebox.showinfo(title="Missing Field", message="Email is empty.")
        return

    if password == "":
        messagebox.showinfo(title="Missing Field", message="Password is empty.")
        return

    reply = messagebox.askyesno(title=website, message=f"These are credentials\n"
                                               f"Email: {email}\n"
                                               f"Password: {password}\n"
                                               f"Are you sure to save?")

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if reply:
        try:
            with open("data.json", "r") as file:
                # Reading from json file
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating data
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

image_canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
image_canvas.create_image(100, 100, image=logo_image)
image_canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "thummarmeet15@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search = Button(text="Search", command=search_password)
search.grid(row=1, column=2)
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)
add = Button(text="Add", width=36, command=save_data)
add.grid(row=4, column=1, columnspan=2)

for child in window.winfo_children():
    child.grid_configure(padx=2, pady=2)

window.mainloop()
