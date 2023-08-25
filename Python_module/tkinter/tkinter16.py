import tkinter as tk
from random import randint, choice

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']


# 创建主窗口
def close():
    window.destroy()


window = tk.Tk()
window.title("字母消除游戏")
window.resizable(False, False)

# 创建画布
canvas = tk.Canvas(window, width=995, height=800)
canvas.config(bg='white')

canvas.pack()

red_line = canvas.create_line(0, 660, 1000, 660, fill='red', width=20)
score = 0
score_label = tk.Label(window, text="得分: 0", font=("Arial", 30))

score_label.pack()

score2 = 0
game_over_label = None

game_over = False


# 定义生成和移动字母的函数
def generate_and_move():
    if not game_over:
        value = choice(letters)
        random_x = randint(10, 990)
        text = canvas.create_text(random_x, 20, text=value, font=("Arial", 24), fill='black')
        move_down(text)
        window.after(400, generate_and_move)  # 随机时间后生成下一个字母


def move_down(text):
    global score
    global score2
    sleep = 20
    canvas.move(text, 0, 1)  # 向下移动1个像素
    if canvas.coords(text)[1] < 635:  # 判断字母是否超出红线范围
        window.after(sleep, move_down, text)  # 每10毫秒调用一次move_down函数，实现连续移动

    else:
        score2 += 1
        if score2 % 5 == 0:
            end_game()
        canvas.delete(text)  # 删除超出范围的字母
        canvas.update()


def key_pressed(event):
    global score
    key = event.char.upper()
    items = canvas.find_all()
    for item in items:
        if canvas.type(item) == 'text' and canvas.itemcget(item, 'text') == key:
            score += 1
            score_label.config(text="得分: " + str(score))
            canvas.delete(item)
            move_down(item)
            canvas.update()
            break


def end_game():
    global game_over, game_over_label
    game_over = True
    canvas.delete("all")
    game_over_label = tk.Label(window, text="你输了", font=("Arial", 60), fg='red')
    game_over_label.pack()
    window.after(3000, restart_game)
    canvas.update()


def restart_game():
    global score, score2, game_over, game_over_label
    score = 0
    score2 = 0
    game_over = False
    score_label.config(text="得分: " + str(score))
    canvas.delete("all")
    if game_over_label is not None:
        game_over_label.pack_forget()
    red_line = canvas.create_line(0, 660, 1000, 660, fill='red', width=20)  # 创建新的红线
    canvas.delete(red_line)  # 删除之前的红线
    canvas.create_line(0, 660, 1000, 660, fill='red', width=20)
    generate_and_move()


# 调用生成和移动字母的函数开始动画
generate_and_move()

# 绑定键盘事件
window.bind('<Key>', key_pressed)

# 运行主循环
window.mainloop()
