import math
import random
import turtle

turtle.speed(0)
turtle.pensize(10)
turtle.up()
turtle.goto(0, 145)
turtle.down()
randius = 150
dig = math.pi / 3
k = 0
for k in range(80):
    turtle.rt(-60)
    randius = randius - 0.05 * randius
    for i in range(0, 7, 1):
        turtle.pencolor(random.random(), random.random(), random.random())
        x = randius * math.sin(i * dig)
        y = randius * math.cos(i * dig)
        turtle.goto(x, y)
turtle.ht()
turtle.done()
