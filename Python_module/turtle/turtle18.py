from random import choice
from turtle import pensize, color, circle, left, ht, speed

pensize(10)
speed(0)
c = ['red', 'orange', 'yellow', 'green', 'blue']
for n in range(350):
    w = choice(c)
    color(w)
    circle(n, 250, 10)
    left(1)
    ht()
