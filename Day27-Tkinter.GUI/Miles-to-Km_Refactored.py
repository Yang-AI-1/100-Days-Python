from tkinter import *

# Improved: Define constants clearly.
# Fixed the assignment syntax. It was likely creating a variable named 'font' unintentionally.
FONT = ("Times New Roman", 16, "bold")
X_PAD = 20
Y_PAD = 20

def calculate():
    try:
        # Improved: Use float() to allow decimal inputs (e.g., 1.5 km)
        kilometer = float(km_input.get())
        miles = kilometer * 0.621371
        
        # Improved: Use the built-in round() function instead of the dunder method __round__
        rounded_miles = round(miles, 2)
        
        digit_label.config(text=f"{rounded_miles}", fg="black")
    except ValueError:
        # Improved: Provide feedback in the UI instead of just printing to the console
        digit_label.config(text="Error", fg="red")
        print("Please input a valid number")

# Creation of the window.
window = Tk()
window.title("Km to Miles Conversion")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20) # Added padding to the window itself for better spacing

# Creation of the Entry.
km_input = Entry(width=10, font=("Arial", 12))
km_input.grid(row=0, column=1)
km_input.focus() # Puts cursor in the box automatically

# Creation of the labels.
km_label = Label(text="Km", font=FONT)
km_label.grid(row=0, column=2)
km_label.config(padx=X_PAD, pady=Y_PAD)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(row=1, column=0)
is_equal_label.config(padx=X_PAD, pady=Y_PAD)

digit_label = Label(text="0", font=FONT)
digit_label.grid(row=1, column=1)
digit_label.config(padx=X_PAD, pady=Y_PAD)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=1, column=2)
miles_label.config(padx=X_PAD, pady=Y_PAD)

# Creation of the button.
calculate_button = Button(text="Calculate", command=calculate, font=("Arial", 12, "bold"))
calculate_button.grid(row=2, column=1)

window.mainloop()
