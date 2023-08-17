import turtle

turtle.speed(1000)


def curvemove():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)


turtle.penup()
turtle.goto(0, -70)
turtle.pendown()

turtle.color('red')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curvemove()
turtle.left(120)
curvemove()
turtle.forward(111.65)
turtle.end_fill()

turtle.penup()
turtle.goto(40, -90)
turtle.pendown()
turtle.write('妈妈我爱你', font=('SimHei', 15, 'bold'))
turtle.hideturtle()
turtle.penup()
turtle.left(140)
turtle.forward(111.65)
for i in range(100):
    turtle.forward(100)
    turtle.right(180)
