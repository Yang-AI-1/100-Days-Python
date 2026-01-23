from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
#Importing an entire class allows us to access all the available methods.
#The question bank holds multiple question objects created.
question_bank = [Question(q["text"], q["answer"]) for q in question_data]  #<--- This is list comprehension method.Its more pythonic
#Instead of adding an empty variable to be looped. We directly assign the loop.

quiz = QuizBrain(question_bank)  #<---- Basically passed in a list that will be the attribute to the quiz object.
while quiz.still_has_questions():  #<--- This method allows us to loop whi
      quiz.next_question()

print("You've completed the quiz!f")
print(f"Your final score was: {quiz.score}/ {quiz.question_number}.")