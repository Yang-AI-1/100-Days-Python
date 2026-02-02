import turtle
import Game_Engine

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


#TODO.Game loop: Prompt, Response, Evaluation, Updating(Score--Title,State-name-placement.

game_on = True
while game_on:
    if Game_Engine.score == 50:
        win_writing = turtle.Turtle()
        win_writing.hideturtle()
        win_writing.penup()
        win_writing.goto(0, 0)
        win_writing.write("YOU WIN!", align="center", font=("Arial", 25, "normal"), move=False)
        break
    answer_state = screen.textinput(Game_Engine.update_title(Game_Engine.score),"What's another state's name?")
    if answer_state is None:
        break
    response_value = Game_Engine.evaluate_response(answer_state)
    if response_value:
        #The game updates the title and the text screen
        Game_Engine.update_state(answer_state)
        Game_Engine.score += 1
    else:
        pass

screen.exitonclick()