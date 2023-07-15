import turtle

turtle.speed(99999999999999999999)
turtle.bgcolor('black')
turtle.width(1)
sides = 4
colors = ["red", "yellow", "blue", "orange", "green", "purple", "brown", "orange", "pink"]
for i in range(2000):
    turtle.pencolor(colors[i % sides])
    turtle.forward(i * 2)
    turtle.left(360 / sides + 1)
turtle.hideturtle()
turtle.penup()
turtle.forward(1000)
turtle.done()
