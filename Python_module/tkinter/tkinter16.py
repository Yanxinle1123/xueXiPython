import tkinter as tk
from random import randint, choice

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

# 创建主窗口
window = tk.Tk()
window.title("字母消除游戏")

# 创建画布
canvas = tk.Canvas(window, width=995, height=800)
canvas.config(bg='white')
canvas.pack()

# 创建红线
red_line = canvas.create_line(0, 660, 1000, 660, fill='red', width=20)


# 定义生成和移动字母的函数
def generate_and_move():
    value = choice(letters)
    random_x = randint(10, 990)
    text = canvas.create_text(random_x, 20, text=value, font=("Arial", 24), fill='black')
    move_down(text)
    window.after(500, generate_and_move)  # 随机时间后生成下一个字母


def move_down(text):
    sleep = 9
    canvas.move(text, 0, 1.5)  # 向下移动1个像素
    if canvas.coords(text)[1] < 635:  # 判断字母是否超出红线范围
        window.after(sleep, move_down, text)  # 每10毫秒调用一次move_down函数，实现连续移动
    else:
        canvas.delete(text)  # 删除超出范围的字母
        canvas.update()


def key_pressed(event):
    key = event.char.upper()
    items = canvas.find_all()
    for item in items:
        if canvas.type(item) == 'text' and canvas.itemcget(item, 'text') == key:
            canvas.delete(item)
            move_down(item)
            canvas.update()
            break


# 绑定键盘事件
window.bind('<Key>', key_pressed)

# 调用生成和移动字母的函数开始动画
generate_and_move()

# 运行主循环
window.mainloop()
