from turtle import *

turtle = Turtle(visible=False)
turtle.speed(10000)
turtle.color("blue", "pink")

for i in range(400):
    turtle.forward(200)
    turtle.left(179)
    turtle.circle(15)
