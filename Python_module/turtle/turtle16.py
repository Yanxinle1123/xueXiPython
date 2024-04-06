import turtle

turtle.pensize(3)
turtle.speed(0)
turtle.bgcolor("black")
colors = ["red", "green", "blue", "yellow"]
for i in range(500):
    turtle.pencolor(colors[i % 4])
    turtle.forward(i * 1)
    turtle.left(90)
turtle.penup()
for i in range(100):
    turtle.hideturtle()
    turtle.forward(50)
    turtle.right(20)
