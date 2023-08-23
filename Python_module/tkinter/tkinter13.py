import random
import tkinter as tk


def close():
    window.destroy()


def change_color(event):
    global text, score, last_text
    if event.char.lower() == text.lower():
        label.config(fg='black')
        label.update()
        window.after(200)
        # 删除当前字母
        label.place_forget()
        label.update()  # 更新窗口，确保旧的Label小部件被完全移除

        # 随机选择一个新字母，确保不与上一个字母相同
        new_text = random.choice(list)
        while new_text == last_text:
            new_text = random.choice(list)
        last_text = text
        text = new_text

        # 创建新的Label小部件，并设置文本和背景颜色
        label.config(text=text, fg='white')
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        print(text)
        if score >= 0:
            score += 1
        score_label.config(text=f"分数: {score}")
    else:
        label.config(fg='white')
        if score > 0:
            score -= 1
        score_label.config(text=f"分数: {score}")


def update_timer():
    global time_left, score
    time_left -= 1
    timer_label.config(text=f"时间: {time_left}", bg='#EF742D', fg='white', font=('Arial', 24))
    if time_left > 0:
        timer_label.after(1000, update_timer)
    else:
        timer_label.config(text="时间到", fg='white', font=('Arial', 48))
        label.place_forget()
        label.update()
        score_label.place_forget()
        score_label.update()
        button.place_forget()  # 隐藏按钮退出
        window.after(2000, show_score)  # 延迟2秒后显示分数


def show_score():
    timer_label.config(text=f"你的分数是{score}", fg='white', font=('Arial', 48))
    window.after(2000, reset_game)  # 延迟2秒后重新开始游戏


def reset_game():
    global time_left, score, last_text
    time_left = 121
    score = 0
    last_text = ""
    score_label.config(text=f"分数: {score}")
    timer_label.config(text=f"时间: {time_left} seconds", bg='#EF742D', fg='white')
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    score_label.place(x=300, y=10)  # 重新显示记分板
    button.place(x=165, y=250)  # 重新显示按钮退出
    window.bind('<Key>', change_color)
    update_timer()


list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']

# 创建主窗口
window = tk.Tk()

# 设置窗口大小
window.geometry("410x300")
window.resizable(False, False)
# 创建一个框架，并设置背景颜色
frame = tk.Frame(window, bg='#EF742D')
frame.pack(fill=tk.BOTH, expand=True)

button = tk.Button(frame, text='退出', fg='black', font=('Arial', 24), command=close)
button.place(x=165, y=250)

# 随机选择一个字符
text = random.choice(list)
last_text = ""

# 创建Label小部件，并设置文本和背景颜色
label = tk.Label(frame, text=text, bg='#EF742D', fg='white', font=('Arial', 24))

# 使用place布局管理器，并设置文本在垂直方向上居中对齐
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# 绑定键盘事件，当用户按下键盘时调用change_color函数
window.bind('<Key>', change_color)

# 添加计时器
time_left = 121
timer_label = tk.Label(window, text=f"时间: {time_left} seconds", bg='#EF742D', fg='white')
timer_label.place(x=10, y=10)

# 添加记分板
score = 0
score_label = tk.Label(window, text=f"分数: {score}", font=('Arial', 24), bg='#EF742D', fg='white')
score_label.place(x=300, y=10)

# 启动计时器
update_timer()

window.mainloop()
