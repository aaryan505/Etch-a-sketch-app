from turtle import Turtle,Screen
tim = Turtle()
screen =Screen()

def move_forward():
    tim.forward(10)
def move_backward() :
     tim.backward(10)
def clockwise():
   new_heading = tim.heading() +10
   tim.setheading(new_heading)
def c_clockwaise():
   new_heading =  tim.heading()-10
   tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
screen.listen()
screen.onkey(key ="w",fun = move_forward )
screen.onkey(key ="s",fun = move_backward )
screen.onkey(key ="a",fun = clockwise )
screen.onkey(key ="d",fun = c_clockwaise )
screen.onkey(key ="c",fun = clear )
screen.exitonclick()
