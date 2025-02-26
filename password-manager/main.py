from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1, columnspan=2)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
email_username_entry = Entry(width=33)
email_username_entry.grid(column=1, row=2, columnspan=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)
password_entry = Entry(width=15)
password_entry.grid(column=1, row=3)

generate_pass_btn = Button(text="Generate Password")
generate_pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()