import random
from tkinter import *
import pandas


BACKGROUND_COLOR = "#B1DDC6"
SMALL_FONT = ("Ariel",40,"italic")
BIG_FONT = ("Ariel", 60, "bold")

current_card = {}
card_info = pandas.read_csv("./data/german_words.csv")
card_records = card_info.to_dict(orient="records")

current_card = random.choice(card_records)

def change_word():
    """Accesses a random german word,writes over the canvas text."""
    global current_card,flip_timer #Global to edit the current card. And the original timer.
    window.after_cancel(flip_timer)
    current_card = random.choice(card_records)
    front_canvas.itemconfig(big_text,text=current_card["German"],fill="black")
    front_canvas.itemconfig(small_text,text= "German",fill="black")
    front_canvas.itemconfig(card_image,image=front_image)
    flip_timer = window.after(4000,func=answer_card)

def answer_card():
    """Flips the card after 5 seconds to give the meaning of the german word."""
    front_canvas.itemconfig(big_text,text=current_card["English"],fill= "white")
    front_canvas.itemconfig(small_text,text="English",fill="white")
    front_canvas.itemconfig(card_image, image=back_image)

def progress():
    """Function removes the current card from the card_records.Adds that card to a new csv file.Removes the
    matching row from the existing csv file by updating the entire card_records dataframe."""
    card_records.remove(current_card) #Removes the card from the current list
    pandas.DataFrame([current_card]).to_csv("./data/known_words.csv", mode="a",header=False)
    pandas.DataFrame(card_records).to_csv("./data/german_words.csv",index=False)
    #Handling the last word
    if not card_records:
        front_canvas.itemconfig(big_text,text="You Win!")
        window.destroy()
    else:
        change_word()


#----------------UI SETUP-------------#
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

#Photo_images.
right_button_image = PhotoImage(file="./images/right.png")
wrong_button_image = PhotoImage(file="./images/wrong.png")
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")

#Buttons.Right button is for known words.Wong button is for signifying you didn't know the word.
right_button = Button(image=right_button_image,highlightthickness=0,command=progress)
right_button.grid(row=1,column=1)

wrong_button = Button(image=wrong_button_image,highlightthickness=0,command=change_word)
wrong_button.grid(row=1,column=0)

#canvas.
front_canvas = Canvas(height=526, width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
card_image = front_canvas.create_image(400, 263, image=front_image)
small_text = front_canvas.create_text(400,150,text="German",font=SMALL_FONT)
big_text = front_canvas.create_text(400,263,text= current_card["German"],font=BIG_FONT)
front_canvas.grid(row=0, column=0, columnspan=2)

#-------------Answer loop---------------#
flip_timer = window.after(4000,func=answer_card)


window.mainloop()