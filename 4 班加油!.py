import math
import turtle as t

t.setup(width=800, height=600)
t.screensize(900, 600, bg='white')
t.bgcolor('pink')
t.pensize(2)
t.speed(1)
t.fillcolor('#57a3c7')
t.begin_fill()
t.circle(120)
t.end_fill()
t.pensize(3)
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()
t.pu()
t.home()
t.goto(0, 134)
t.pd()
t.pensize(4)
t.pensize(4)
t.fillcolor("#EA0014")
t.begin_fill()
t.circle(18)
t.end_fill()
t.pu()
t.goto(-2, 155)
t.pensize(2)
t.color('white', 'white')
t.pd()
t.begin_fill()
t.circle(4)
t.end_fill()
t.pu()
t.goto(-30, 160)
t.pensize(4)
t.pd()
t.color('black', 'white')
t.begin_fill()
a = 0.4
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.08
        t.lt(3)
        t.fd(a)
t.end_fill()
t.pu()
t.goto(30, 160)
t.pensize(4)
t.pd()
t.color('black', 'white')
t.begin_fill()
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.08
        t.lt(3)
        t.fd(a)
t.end_fill()
t.pu()
t.goto(-38, 190)
t.pensize(8)
t.pd()
t.right(-30)
t.forward(15)
t.right(70)
t.forward(15)
t.pu()
t.goto(15, 185)
t.pensize(4)
t.pd()
t.color('black', 'black')
t.begin_fill()
t.circle(13)
t.end_fill()
t.pu()
t.goto(13, 190)
t.pensize(2)
t.pd()
t.color('white', 'white')
t.begin_fill()
t.circle(5)
t.end_fill()


def Draw_Arc(t1, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    Arc_Line(t1, n, step_length, step_angle)


def Arc_Line(t1, n, length, angle):
    for index in range(n):
        t1.fd(length)
        t1.lt(angle)


t.pu()
t.goto(-60, 80)
t.pd()
step = 1
t.setheading(270)
t.fillcolor("#EA0014")
t.begin_fill()
Draw_Arc(t, 60, 190)
t.setheading(180)
t.forward(120)
t.end_fill()
t.pu()
t.goto(2, 60)
t.setheading(120)
t.fillcolor("#EA0014")
t.pd()
t.begin_fill()
Draw_Arc(t, 25, 170)
t.pu()
t.goto(45, 40)
t.setheading(70)
t.pd()
Draw_Arc(t, 25, 170)
t.pu()
t.pencolor("black")
t.goto(-44, 40)
t.setheading(305)
t.pd()
Draw_Arc(t, 53, 125)
t.end_fill()
t.pensize(2)
t.pencolor("#57a3c7")
t.pu()
t.goto(-70, 35)
t.setheading(265)
t.fillcolor("#57a3c7")
t.begin_fill()
t.pd()
for y in range(50):
    if y > 10:
        t.pencolor("black")
    if y < 35:
        t.left(0.3)
    else:
        t.right(0.3)
    t.forward(3)
t.setheading(0)
t.forward(60)
t.setheading(70)
t.forward(25)
t.setheading(90)
t.forward(90)
t.setheading(160)
t.forward(78)
t.end_fill()
