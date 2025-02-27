from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: " f"\nEmail: {email_username}"
                                                     f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
                with open("data.txt", "a") as f:
                    f.write(f"{website} | {email_username} | {password}\n")
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website:")
email_username_label = Label(text="Email/Username:")
pass_label = Label(text="Password:")

#Entries
website_entry = Entry(width=33)
email_username_entry = Entry(width=33)
email_username_entry.insert(0, "taison@email.com")
password_entry = Entry(width=15)

#Btuttons
generate_pass_btn = Button(text="Generate Password")
add_btn = Button(text="Add", width=36, command=save)

website_entry.grid(column=1, row=1, columnspan=2)
website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
email_username_entry.grid(column=1, row=2, columnspan=2)
pass_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3)
generate_pass_btn.grid(column=2, row=3)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()