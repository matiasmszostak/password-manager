from tkinter import *

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
email_entry = Entry(width=41)
email_entry.grid(column=1, row=2, columnspan=2, sticky="W", pady=5)
password_entry = Entry(width=22)
password_entry.grid(column=1, row=3, sticky="W", pady=5)

# Buttons
generate_pass_button = Button(text="Generate Password", width=14)
generate_pass_button.grid(column=2, row=3, sticky="W", padx=5)
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2, pady=10)

window.mainloop()
