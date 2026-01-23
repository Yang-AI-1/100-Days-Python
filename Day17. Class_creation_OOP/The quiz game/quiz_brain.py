#TODO.Asking questions.
#TODO.Checking if the answer was correct.
#TODO.Checking if at the end of the quiz.

class QuizBrain:
    def __init__(self, questions_list):
        """ The Object will start from the first question number. And hold the current question from the list"""
        self.score = 0
        self.question_number = 0  #This is how attributes of objects are added.
        self.question_list = questions_list #This means that the list passed into the initial creation of the object adds that list to the object as an attribute.
    def still_has_questions(self):
        """ Returns the Boolean of the expression below. To evaluate whether we need to continue going to the next question."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Will pull up the question from the selected question number."""
        current_question = self.question_list[self.question_number] #<-- Current question is an object fetched form the arranged list.
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):") #<--- Q{Number of question} : {The text of the current question object selected from the list} Prompt the user to answer true or false.
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

#The check answer method has been used globally in this file even before referencing hierarchy. That's the kink of using classes.
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")



