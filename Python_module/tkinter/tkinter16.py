from random import randint, choice
from tkinter import *

from comm.comm_music import stop_music, play_music_with_window2

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
grade_list = [
    {"sleep": 20, "other_char": 0, "down_speed": 600},  # 第 1 关
    {"sleep": 15, "other_char": 0, "down_speed": 600},  # 第 2 关
    {"sleep": 10, "other_char": 0, "down_speed": 600},  # 第 3 关
    {"sleep": 20, "other_char": 1, "down_speed": 500},  # 第 4 关
    {"sleep": 20, "other_char": 2, "down_speed": 500},  # 第 5 关
    {"sleep": 20, "other_char": 3, "down_speed": 500},  # 第 6 关
    {"sleep": 15, "other_char": 2, "down_speed": 400},  # 第 7 关
    {"sleep": 15, "other_char": 3, "down_speed": 400},  # 第 8 关
    {"sleep": 10, "other_char": 5, "down_speed": 300},  # 第 9 关
    {"sleep": 10, "other_char": 8, "down_speed": 250},  # 第 10 关
]
grade = 0
grade_map = grade_list[grade]

window = Tk()
window.title("字母消除游戏")
window.resizable(False, False)

canvas = Canvas(window, width=995, height=800)
canvas.config(bg='white')
canvas.pack()

red_line = canvas.create_line(0, 660, 1000, 660, fill='red', width=20)
score = 0
score_label = Label(window, text="得分: 0", font=("Arial", 30))
score_label.pack()

grade_label = Label(window, text="第{}关".format(grade + 1), font=("Arial", 20))
grade_label.pack()

score2 = 0
game_over_label = None
game_over = False
quantity = 0


def move_down(text, is_del=False):
    global score, score2
    sleep = grade_map["sleep"]
    canvas.move(text, 0, 1)
    print(f"is_del={is_del}|text={text}|canvas.coords(text)={canvas.coords(text)}")
    if not is_del and not canvas.coords(text) and canvas.coords(text)[1] < 635:
        window.after(sleep, move_down, text)
    else:
        score2 += 1
        if score2 % 5 == 0:
            end_game()
        canvas.delete(text)
        canvas.update()


def key_pressed(event):
    global score, quantity
    key = event.char.upper()
    items = canvas.find_all()
    for item in items:
        if canvas.type(item) == 'text' and canvas.itemcget(item, 'text') == key:
            score += 1
            quantity += 1
            if quantity >= 4:
                generate_extra_letters()
                quantity = 0
            if score >= 100:
                winning_the_game()
                quantity = 0
            score_label.config(text="得分: " + str(score))
            canvas.delete(item)
            move_down(item)
            canvas.update()
            break


def generate_and_move():
    if not game_over:
        value = choice(letters)
        random_x = randint(20, 980)
        text = canvas.create_text(random_x, 20, text=value, font=("Arial", 24), fill='black')
        move_down(text)
        window.after(grade_map["down_speed"], generate_and_move)


def generate_extra_letters():
    for _ in range(grade_map["other_char"]):
        value = choice(letters)
        random_x = randint(20, 980)
        text = canvas.create_text(random_x, 20, text=value, font=("Arial", 24), fill='black')
        move_down(text)


def end_game():
    global game_over, game_over_label, grade, grade_map
    game_over = True
    canvas.delete("all")
    game_over_label = Label(window, text=f"你输了,grade={grade + 1}|grade_map={grade_map}",
                            font=("Arial", 60), fg='red')
    game_over_label.pack()

    grade = 0
    grade_map = grade_list[grade]

    window.after(2000, restart_game)
    canvas.update()


def winning_the_game():
    global game_over, grade, grade_map
    game_over = True
    canvas.delete("all")
    # 增加关卡
    grade = grade + 1
    if grade == 10:
        grade = 0
    grade_map = grade_list[grade]

    window.after(600, restart_game)
    canvas.update()


def restart_game():
    global score, score2, game_over, game_over_label, red_line, grade_map
    score = 0
    score2 = 0
    game_over = False
    score_label.config(text="得分: " + str(score))
    grade_label.config(text="第{}关".format(grade + 1))
    # grade_label.config(text=f"第{grade + 1}关，参数：{grade_map}")
    canvas.delete("all")
    if game_over_label is not None:
        game_over_label.pack_forget()
    red_line = canvas.create_line(0, 660, 1000, 660, fill='red', width=20)
    canvas.delete(red_line)
    canvas.create_line(0, 660, 1000, 660, fill='red', width=20)
    generate_and_move()


def on_close():
    stop_music()
    window.destroy()


generate_and_move()
window.bind('<Key>', key_pressed)

music_file = "./Joachim Neuville - Arena [mqms].ogg"
play_music_with_window2(window, music_file, 10000, False)

window.mainloop()
