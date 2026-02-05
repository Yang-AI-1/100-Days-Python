from tkinter import *

FONT = font=("Times New Roman", 16 ,"bold")
x_pad = 20
y_pad = 20

def calculate():
    try:
     kilometer = float(km_input.get()) #Using the float conversion consideres if the user wants to know specific decimal pointers.
     miles = kilometer * 0.621371
     digit_label.config(text=f"{miles.__round__(2)}")
    except ValueError:
        print("Input a value")

#Creation of the window.
window = Tk()
window.title("Km to Miles Conversion")
window.minsize(width=200,height=200)

#Creation of the labels. 4 in total.
km_label = Label(text="Km",font=FONT)
km_label.grid(row=0,column=2) #2 is the third index.
km_label.config(padx=x_pad,pady=y_pad)

miles_label = Label(text="Miles",font=FONT)
miles_label.grid(row=1,column=2)
miles_label.config(padx=x_pad,pady=y_pad)

digit_label = Label(text= "0", font=FONT)
digit_label.grid(row=1,column=1)
digit_label.config(padx=x_pad,pady=y_pad)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(row=1,column=0)
is_equal_label.config(padx=x_pad,pady=y_pad)

# Creation of the Entry.
km_input = Entry(width=10)
km_input.grid(row=0,column=1)

# Creation of the button.
calculate_button = Button(text="Calculate",command=calculate) #Functions passed in as parameters are not bracketed.
calculate_button.grid(row=2,column=1)

window.mainloop()