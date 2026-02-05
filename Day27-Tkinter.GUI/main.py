from tkinter import *

def change_label():
    my_label.config(text=input.get()) #Objects have global scope??!!


window = Tk() #screen class. Created screen object called window.
window.title("My First Programme!!")
window.minsize(width=500,height=500)

#Label. Just a writing on the screen.

my_label = Label(text="New Label",font=("Times New Roman", 24 ,"bold")) #Label object has been created.
# my_label.pack() #Has been specified how it's laid out.
my_label.grid(column=0 ,row= 0)

#Entry - Basically gives you a place to input text.
input = Entry(width=10)
# input.pack() #To place the input window.
input.grid(row=2, column=3)

#Button. Clickable buttons on the GUI.

button = Button(text= "Click me") #object(button) creation and initialization
button.config(text= "Click here", command=change_label) #You can use the config method to initialize. It'll follow vertical execution order
# button.pack() #It appears that the pack method doesn't require to be in any particular position.
button.grid(row=1,column=1)

new_button = Button(text="Click me.")
new_button.grid(row=0, column=2)

window.mainloop() #This line of code should be at the end of the programme. It keeps the window opem


