import turtle

turtle.bgcolor('white')
turtle.width(2)
sides = 5
colors = ["purple", "brown", "grey", "indigo", "papayawhip"]
for x in range(60):
    turtle.pencolor(colors[x % sides])
    turtle.forward(x * 2)
    turtle.left(360 / sides + 1)
