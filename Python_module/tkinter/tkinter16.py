from random import randint, choice
from tkinter import Tk, Canvas, Label

from comm.comm_music import play_music_with_window2, quit_music, change_music

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
is_game_over = False
quantity = 0

# music_ret_id_first = None
music_ret_id_mid = None
music_ret_id_last = None


def move_down(text):
    global score, score2
    sleep = grade_map["sleep"]
    # y_speed = 1 + (600 - grade_map["down_speed"])
    canvas.move(text, 0, 1)
    coords_list = canvas.coords(text)
    # print(f"text={text}|coords_list={coords_list}")
    if coords_list:
        if canvas.coords(text)[1] < 635:
            window.after(sleep, move_down, text)
        else:
            score2 += 1
            if score2 % 5 == 0:
                lost_game()
            canvas.delete(text)
            canvas.update()
    else:
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
            if score >= (grade + 1) * 10:
                winning_the_game()
                quantity = 0
            score_label.config(text=f"得分: {score}")
            canvas.delete(item)
            canvas.update()
            break


def generate_and_move():
    if not is_game_over:
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


def lost_game():
    global is_game_over, game_over_label, grade, grade_map, score, score2, red_line, music_ret_id_first, quantity
    is_game_over = True
    canvas.delete("all")
    red_line = canvas.create_line(0, 660, 1000, 660, fill='red', width=20)
    game_over_label = Label(window, text="你输了",
                            font=("Arial", 60), fg='red')
    game_over_label.pack()

    if grade > 4:
        # music_ret_id = None
        if grade < 8:
            music_ret_id = music_ret_id_mid
        else:
            music_ret_id = music_ret_id_last

        music_ret_id_first = change_music(win, music_file_start, 290000,
                                          True, True, music_ret_id)

    grade = 0
    grade_map = grade_list[grade]

    score = 0
    score2 = 0
    quantity = 0
    window.after(2000, restart_game)
    canvas.update()


def winning_the_game():
    global is_game_over, grade, grade_map, music_ret_id_first, music_ret_id_mid, music_ret_id_last, quantity, score
    is_game_over = False
    canvas.delete("all")
    # 增加关卡
    grade = grade + 1
    if grade == 10:
        grade = 0
        score = 0

    if grade == 0:
        music_ret_id_first = change_music(win, music_file_start, 290000,
                                          True, True, music_ret_id_last)
    elif grade == 5:
        music_ret_id_mid = change_music(win, music_file_mid, 290000,
                                        True, True, music_ret_id_first)
    elif grade == 8:
        music_ret_id_last = change_music(win, music_file_last, 290000,
                                         True, True, music_ret_id_mid)
    grade_map = grade_list[grade]

    window.after(60, restart_game)
    canvas.update()


def restart_game():
    global score, score2, is_game_over, game_over_label, red_line, grade_map, quantity
    # score = 0
    score2 = 0
    quantity = 0
    score_label.config(text=f"得分: {score} ")
    # info = f"第 {grade + 1} 关"
    info = f"第 {grade + 1} 关 ->参数:{grade_map}"
    grade_label.config(text=info)

    canvas.delete("all")
    if game_over_label is not None:
        game_over_label.pack_forget()
    red_line = canvas.create_line(0, 660, 1000, 660, fill='red', width=20)
    quantity = 0
    # generate_and_move()


def on_close():
    quit_music()
    win.destroy()
    window.destroy()


generate_and_move()
window.bind('<Key>', key_pressed)

music_file_start = "./game_music_start.ogg"
music_file_mid = "./game_music_mid_forever.mp3"
music_file_last = "./game_music_last.mp3"
win = Tk()

music_ret_id_first = play_music_with_window2(win, music_file_start, 290000,
                                             True, True)

# play_music_with_window2(win, music_file_mid, 290000,
#                         True, True)

window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()
