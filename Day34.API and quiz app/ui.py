from tkinter import *
from quiz_brain import QuizBrain
import os

THEME_COLOR = "#375362"
TEXT_FONT = ("Arial",20,"italic")

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)

        self.score_label = Label(text="Score: 0",bg=THEME_COLOR,font=TEXT_FONT,fg="white")
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(height=250,width=300)
        self.question_text = self.canvas.create_text(150,125,text="Wow",font=TEXT_FONT,fill=THEME_COLOR,width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        # Construct absolute path to images to avoid FileNotFoundError
        base_path = os.path.dirname(__file__)
        
        self.true_image = PhotoImage(file=os.path.join(base_path, "images/true.png"))
        self.tick_button = Button(image=self.true_image,padx=20,pady=20,highlightthickness=0,command=self.choice_true)
        self.tick_button.grid(row=2,column=0)

        self.false_image = PhotoImage(file=os.path.join(base_path, "images/false.png"))
        self.false_button = Button(image=self.false_image,padx=20,pady=20,highlightthickness=0,command=self.choice_false)
        self.false_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.tick_button.config(state="disabled")
            self.false_button.config(state="disabled")
            
    def choice_true(self):
        """Passes in true to the check_answer method from the quiz brain"""
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def choice_false(self):
        """Passes in false to the check_answer method from quiz brain."""
        self.give_feedback(self.quiz.check_answer(user_answer="False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000,self.get_next_question)
