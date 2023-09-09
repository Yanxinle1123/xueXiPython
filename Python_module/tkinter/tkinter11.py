import tkinter as tk


# from Python_module.tkinter.tkinter20 import ball_to


def move_rectangle(event):
    key = event.keysym
    window_width = canvas.winfo_width() - 10
    window_height = canvas.winfo_height() - 10
    x1, y1, x2, y2 = canvas.coords(rectangle)
    if key == 'Up' and y1 > 10:
        canvas.move(rectangle, 0, -10)
    elif key == 'Down' and y2 < window_height:
        canvas.move(rectangle, 0, 10)
    elif key == 'Left' and x1 > 10:
        canvas.move(rectangle, -10, 0)
    elif key == 'Right' and x2 < window_width:
        canvas.move(rectangle, 10, 0)


def resize_canvas(event):
    canvas.config(width=event.width, height=event.height)


# 创建主窗口
window = tk.Tk()
window.title('移动矩形')
window.geometry('1000x800')
window.resizable(False, False)

# 创建Canvas小部件
canvas = tk.Canvas(window, width=1000, height=800)
canvas.pack()

# 创建矩形
rectangle = canvas.create_rectangle(100, 100, 200, 200, fill='red')

# 绑定键盘事件
canvas.bind('<KeyPress>', move_rectangle)

# 绑定窗口大小变化事件
window.bind('<Configure>', resize_canvas)

# 设置焦点在Canvas上，以便捕获键盘事件
canvas.focus_set()
# ball_to(canvas, 900, 50, pixel=5, sleep_ms=1)
window.mainloop()
