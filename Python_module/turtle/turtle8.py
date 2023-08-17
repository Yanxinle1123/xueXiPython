import turtle

turtle.pensize(2)
turtle.speed(1)
turtle.bgcolor("green")
turtle.color("red", "yellow")
turtle.begin_fill()
for i in range(5):
    turtle.pencolor("red")
    turtle.forward(100)
    turtle.right(144)
turtle.end_fill()
turtle.forward(100)
turtle.right(144)
