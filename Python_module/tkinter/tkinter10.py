import tkinter as tk


def draw_square():
    canvas.create_rectangle(50, 50, 150, 150, outline='black', fill='red')


# 创建主窗口
window = tk.Tk()
window.title('绘制正方形')

# 创建Canvas小部件
canvas = tk.Canvas(window, width=200, height=200)
canvas.pack()

# 创建绘制按钮
draw_button = tk.Button(window, text='绘制正方形', command=draw_square)
draw_button.pack()

window.mainloop()
