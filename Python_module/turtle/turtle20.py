import turtle

# 创建画布和画笔
canvas = turtle.Screen()
canvas.bgcolor("black")
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")

# 绘制玫瑰花
for _ in range(36):
    pen.forward(100)
    pen.right(45)
    pen.forward(100)
    pen.right(135)
    pen.forward(100)
    pen.right(45)
    pen.forward(100)
    pen.right(135)
    pen.right(10)

# 结束绘画
pen.forward(1000)
