import turtle

t = turtle
t.speed(0)
t.hideturtle()
t.pencolor("brown")
t.pensize(3)
t.bgcolor("black")
for i in range(10000):
    t.forward(i + 1)
    t.right(90)
