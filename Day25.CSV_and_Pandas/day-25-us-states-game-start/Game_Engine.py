import pandas
import turtle

states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.tolist()

TOTAL_STATES = len(states_list)

score = 0
guessed_states = []

def evaluate_response(user_response):
    """Compares the users response to the states available"""
    if user_response.title() in states_list and user_response.title() not in guessed_states:
        guessed_states.append(user_response.title())
        return True
    return None


def update_state(correct_response):
    """Takes the correct user response and maps it onto the screen"""
    specific_state_row= states_data[states_data.state == correct_response]
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(int(specific_state_row.x.item()), int(specific_state_row.y.item()))
    new_turtle.write(correct_response)

def update_title(game_score):
    """Updates the title the game."""
    title = f"{game_score}/{TOTAL_STATES} guessed correctly"
    return title







