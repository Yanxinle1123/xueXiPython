import turtle


def paint():
    """
    Draw a square using Turtle lib in python
    """
    turtle.penup()
    turtle.goto(-100, -100)
    turtle.pendown()
    turtle.begin_fill()

    turtle.forward(100)
    turtle.right(90)

    turtle.forward(100)
    turtle.right(90)

    turtle.forward(100)
    turtle.right(90)

    turtle.forward(100)
    turtle.right(90)


# generate main program
if __name__ == "__main__":
    # paint the square
    paint()
