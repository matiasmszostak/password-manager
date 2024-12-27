from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askokcancel


# ---------------------------- UI SETUP ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()


    if "" == website or "" == email or "" == password:
        messagebox.showerror(title="Error", message="Please, don't leave any empty fields!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=("These are the details entered:\n"
                                                       f"Website {website}\n"
                                                       f"Email: {email}\n"
                                                       f"Password: {password}\n"
                                                       f"Is it ok to save?"))
        if is_ok:

            with open("passwords.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

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
generate_pass_button = Button(text="Generate Password", width=14)
generate_pass_button.grid(column=2, row=3, sticky="W", padx=5)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, pady=10)

window.mainloop()
