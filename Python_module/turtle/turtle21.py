import turtle

turtle.pensize(1)
turtle.speed(0)
turtle.fillcolor('red')
turtle.begin_fill()
turtle.pencolor('blue')
turtle.bgcolor('yellow')
for i in range(500):
    turtle.forward(i + 1)
    turtle.right(90)
turtle.hideturtle()
turtle.end_fill()
turtle.done()
