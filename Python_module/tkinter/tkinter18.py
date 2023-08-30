import random
import tkinter as tk
import tkinter.font as tkfont

pushed_button = []

number = 0


def close():
    window.destroy()


game_over = False


def key_pressed(event):
    global number, score, label1, label2, label3, label4, label5, value1, value2, value3, value4, value5
    key = event.keysym.upper()
    # print(f"before: key = {key} | number = {number} | pushed_button = {pushed_button}")
    if game_over:  # 如果游戏结束，不执行后续代码
        return
    elif key == pushed_button[0]:
        label1.config(fg='black')
        number += 1
    elif key == pushed_button[1] and number == 1:
        label2.config(fg='black')
        number += 1
    elif key == pushed_button[2] and number == 2:
        label3.config(fg='black')
        number += 1
    elif key == pushed_button[3] and number == 3:
        label4.config(fg='black')
        number += 1
    elif key == pushed_button[4] and number == 4:
        label5.config(fg='black')
        number = 0
        score += 1
        # print(f'pushed_button = {pushed_button}')
        # print(f"after: key = {key} | number = {number} | pushed_button = {pushed_button}")
        score_label.config(text=f"分数: {score}")
        value1, value2, value3, value4, value5 = random_value()
        label1.config(text=value1, fg='white')
        label2.config(text=value2, fg='white')
        label3.config(text=value3, fg='white')
        label4.config(text=value4, fg='white')
        label5.config(text=value5, fg='white')


def show_final_score():
    global game_over
    game_over = True
    timer_label.config(text="时间到", fg='red', font=('Arial', 150))
    window.after(2000, lambda: timer_label.config(text="时间到", fg='red', font=('Arial', 50)))
    window.after(4000, lambda: score_label.config(text=f'你的分数是: {score}', fg='red', font=('Arial', 100)))
    window.after(6000, lambda: score_label.config(text=f'你的分数是: {score}', fg='red', font=('Arial', 50)))
    window.after(8000, lambda: reset_game())  # 添加此行来重置游戏状态


def reset_game():
    global game_over, time_left, score
    game_over = False
    time_left = 121
    score = 0
    score_label.config(text=f"分数: {score}", font=('Arial', 50), bg='#6322D6', fg='white')
    timer_label.config(text=f"时间: {time_left}", font=('Arial', 50), bg='#6322D6', fg='white')
    update_timer()


def update_timer():
    global time_left, score_label, score
    time_left -= 1
    timer_label.config(text=f"时间: {time_left}", bg='#6322D6', fg='white', font=('Arial', 50))
    if time_left > 0:
        timer_label.after(1000, update_timer)
    else:
        show_final_score()


def random_value():
    value_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
    while True:
        random_values = random.sample(value_list, 5)
        if len(set(random_values)) == 5:
            value1 = random_values[0]
            value2 = random_values[1]
            value3 = random_values[2]
            value4 = random_values[3]
            value5 = random_values[4]
            pushed_button.clear()
            pushed_button.append(value1)
            pushed_button.append(value2)
            pushed_button.append(value3)
            pushed_button.append(value4)
            pushed_button.append(value5)
            print(f'pushed_button = {pushed_button}')
            return value1, value2, value3, value4, value5


window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = screen_width // 2 - 1000 // 2
position = f'1000x800+{window_width}+100'
window.geometry(position)
window.config(bg='#6322D6')
value1, value2, value3, value4, value5 = random_value()
label3 = tk.Label(window, text=value3, bg='#6322D6', font=('Arial', 80), fg='white')

# 获取label的文本宽度
label_font = tkfont.Font(font=label3['font'])
text_width = label_font.measure(value3)

label3.place(x=1000 // 2 - text_width // 2, y=300)
label2 = tk.Label(window, text=value2, bg='#6322D6', font=('Arial', 80), fg='white')
label2.place(x=(1000 // 2 - text_width // 2) - 80, y=300)
label1 = tk.Label(window, text=value1, bg='#6322D6', font=('Arial', 80), fg='white')
label1.place(x=(1000 // 2 - text_width // 2) - 160, y=300)
label4 = tk.Label(window, text=value4, bg='#6322D6', font=('Arial', 80), fg='white')
label4.place(x=(1000 // 2 - text_width // 2) + 80, y=300)
label5 = tk.Label(window, text=value5, bg='#6322D6', font=('Arial', 80), fg='white')
label5.place(x=(1000 // 2 - text_width // 2) + 160, y=300)

button = tk.Button(window, text='退出', font=('Arial', 80), command=close)
button.place(x=400, y=650)

# 添加记分板
score = 0
score_label = tk.Label(window, text=f"分数: {score}", font=('Arial', 50), bg='#6322D6', fg='white')
score_label.place(x=250, y=10)

# 添加计时器
time_left = 121
timer_label = tk.Label(window, text=f"时间: {time_left}", font=('Arial', 50), bg='#6322D6', fg='white')
timer_label.place(x=10, y=10)

update_timer()

window.bind("<Key>", key_pressed)
window.mainloop()
