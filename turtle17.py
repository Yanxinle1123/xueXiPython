import turtle

turtle.pensize(4)
turtle.speed(1000)
turtle.bgcolor('black')
turtle.pencolor('white')
for i in range(3600):
    turtle.forward(i + 1)
    turtle.right(90)
