import tkinter as tk


def on_mouse_down(event):
    # 鼠标按下时的回调函数
    global prev_x, prev_y
    prev_x = event.x
    prev_y = event.y
    canvas.bind('<B1-Motion>', on_mouse_move)


def on_mouse_move(event):
    # 鼠标移动时的回调函数
    global prev_x, prev_y
    if is_inside_rectangle(event.x, event.y):
        dx = event.x - prev_x
        dy = event.y - prev_y
        canvas.move(rect, dx, dy)
        prev_x = event.x
        prev_y = event.y


def is_inside_rectangle(x, y):
    # 判断坐标 (x, y) 是否在矩形内部
    rect_coords = canvas.coords(rect)
    rect_x1, rect_y1, rect_x2, rect_y2 = rect_coords
    if rect_x1 <= x <= rect_x2 and rect_y1 <= y <= rect_y2:
        return True
    return False


# 创建Tkinter窗口和画布
root = tk.Tk()
root.resizable(False, False)
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# 创建一个矩形
rect = canvas.create_rectangle(50, 50, 150, 150, fill='blue')

# 绑定鼠标按下事件
canvas.bind('<Button-1>', on_mouse_down)

# 运行Tkinter事件循环
root.mainloop()
