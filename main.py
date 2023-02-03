from tkinter import *
from tkinter import messagebox
import random
import string
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

def password_generator():
    if password_entry.get() == '':
        passw = generate_password(16)
        password_entry.insert(0, passw)

print(generate_password(16))
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) < 3 or len(password) < 3:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty \nnor put an incorrect email address.")
    else:
        is_ok = messagebox.askyesno(title=website,
                                    message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{website} | {email} | {password} \n')
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'hbotema1616@gmail.com')
password_entry = Entry(width=21,)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()