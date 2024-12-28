from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json



# ---------------------------- GENERATE PASSWORD ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)
    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }


    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please, don't leave any empty fields!")

    else:
        try:
            with open("passwords.txt", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}
        data.update(new_data)

        with open("passwords.txt", "w") as data_file:
            json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.geometry("500x400")

# Canvas
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=logo_img.width(), height=logo_img.height())
canvas.create_image(logo_img.width() // 2, logo_img.height() // 2, image=logo_img)
canvas.grid(column=1, row=0, columnspan=2)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="E", pady=5)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="E", pady=5)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="E", pady=5)

# Entries
website_entry = Entry(width=41)
website_entry.grid(column=1, row=1, columnspan=2, sticky="W", pady=5)
website_entry.focus()
email_entry = Entry(width=41)
email_entry.grid(column=1, row=2, columnspan=2, sticky="W", pady=5)
email_entry.insert(0, "matiasmszostak@gmail.com")
password_entry = Entry(width=22)
password_entry.grid(column=1, row=3, sticky="W", pady=5)

# Buttons
generate_pass_button = Button(text="Generate Password", width=14, command=generate_password)
generate_pass_button.grid(column=2, row=3, sticky="W", padx=5)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, pady=10)

window.mainloop()
