from tkinter import *
from tkinter import  messagebox
from random import randint,choice,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project from day 5 ^_^.
def generate_password():
    """Generates a random password"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for lett in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symb in range(randint(8, 10))]
    password_numbers = [choice(numbers) for numb in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password) #Places my password Immediately into my clip board for ready pasting.

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """Once called it adds contents of the website,Email and password entries to a .txt file in a nice readable format."""
    website = website_entry.get()
    email = email_username_entry.get()
    user_password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Error", message="Make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website , message=f"These are the details of the entries: \nEmail: {email}"
                                                            f"\nPassword: {user_password} \nIs it ok to save?")
        if is_ok:
            with open("passwords.txt", "a+") as password_file:
                password_file.write(website + " | " + email + " | " +user_password + "\n") #Couldv used an f string instead but okay.
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50,pady=50)
window.title("Password Manager")

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200,width=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

#Labels
website_label = Label(text="Website:",font=("Courier", 12 ,"bold"))
website_label.grid(row=1,column=0)

email_username_label =  Label(text="Email/Username:",font=("Courier", 12 ,"bold"))
email_username_label.grid(row=2,column=0)

password_label = Label(text="Password:",font=("Courier", 12 ,"bold"))
password_label.grid(row=3,column=0)

#Entries.
website_entry = Entry(width=42)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=42)
email_username_entry.grid(row=2,column=1,columnspan=2)
email_username_entry.insert(0, "etyangdylanokomol@gmail.com" )

password_entry = Entry(width=24)
password_entry.grid(row=3,column=1)

#Button.
add_button = Button(text="Add",width=35,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)

passgen_button = Button(text="Generate password",command=generate_password)
passgen_button.grid(row=3,column=2)

window.mainloop()