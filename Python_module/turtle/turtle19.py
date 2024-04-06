from turtle import Turtle

turtle = Turtle(visible=False)
turtle.speed(0)
turtle.color("blue", "pink")

for i in range(400):
    turtle.forward(200)
    turtle.left(179)
    turtle.circle(15)
