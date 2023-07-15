import turtle

turtle.speed(1000)
turtle.bgcolor('black')
turtle.width(1)
sides = 2
for i in range(5000):
    turtle.pencolor('purple')
    turtle.forward(i * 2)
    turtle.left(360 / sides + 1)
turtle.hideturtle()
turtle.penup()
for i in range(500):
    turtle.forward(1000)
turtle.down()
