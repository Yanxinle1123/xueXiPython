from random import *
from turtle import *

pensize(10)
speed(10000)
c = ['red', 'orange', 'yellow', 'green', 'blue']
for n in range(350):
    w = choice(c)
    color(w)
    circle(n, 250, 10)
    left(1)
    ht()
