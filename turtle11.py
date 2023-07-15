import turtle

turtle.hideturtle()
turtle.pensize(2)
turtle.speed(1000)
turtle.bgcolor("black")
colors = ["red", "green", "blue", "yellow"]
for i in range(200):
    turtle.pencolor(colors[i % 4])
    turtle.forward(i * 2)
    turtle.left(90)
turtle.penup()
for i in range(100):
    turtle.forward(100000000000000)
    turtle.right(20)
