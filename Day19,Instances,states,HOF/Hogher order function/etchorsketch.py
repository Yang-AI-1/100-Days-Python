import turtle
from turtle import Turtle,Screen

tod = Turtle()

screen = Screen()


def forward():
    tod.forward(10)

def backward():
    tod.backward(10)

def right():
    tod.right(10)

def left():
    tod.left(10)

def clear():
    screen.reset()

screen.listen()
screen.onkeypress(fun=forward,key="w")
screen.onkeypress(fun=backward,key="s")
screen.onkeypress(fun=right,key="d")
screen.onkeypress(fun=left,key="a")
screen.onkeypress(fun=clear,key="c")
screen.exitonclick()

