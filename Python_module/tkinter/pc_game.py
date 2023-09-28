import os
import random
import sys
import uuid
from random import randint, choice
from tkinter import Tk, Canvas, Label, Button, Toplevel, HORIZONTAL, Scale

import pygame

from comm.comm_draw import ball_to, get_text_center_coords, ball_first, change_ball_color
from comm.comm_music import play_music_by_window, quit_music, change_music

# if not sys.stdout:
#     sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)

number = 0
number2 = 1
if_game_start = False
yellow = '#E8BA36'
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

rainbow = f'red,blue,{yellow}'
two_color = "red,blue"
grade_list = [
    {"move_char_time_ms": 20, "other_char": 0, "gen_char_time_ms": 600,
     "ball_color": "red", "char_color": "red"},  # 第 1 关
    {"move_char_time_ms": 15, "other_char": 0, "gen_char_time_ms": 600,
     "ball_color": "red", "char_color": "red"},  # 第 2 关
    {"move_char_time_ms": 10, "other_char": 0, "gen_char_time_ms": 600,
     "ball_color": "blue", "char_color": "blue"},  # 第 3 关
    {"move_char_time_ms": 20, "other_char": 1, "gen_char_time_ms": 500,
     "ball_color": "blue", "char_color": two_color},  # 第 4 关
    {"move_char_time_ms": 20, "other_char": 2, "gen_char_time_ms": 500,
     "ball_color": "red", "char_color": two_color},  # 第 5 关
    {"move_char_time_ms": 20, "other_char": 3, "gen_char_time_ms": 500,
     "ball_color": "red", "char_color": two_color},  # 第 6 关
    {"move_char_time_ms": 15, "other_char": 2, "gen_char_time_ms": 400,
     "ball_color": yellow, "char_color": f"{yellow},red"},  # 第 7 关
    {"move_char_time_ms": 15, "other_char": 3, "gen_char_time_ms": 400,
     "ball_color": "blue", "char_color": rainbow},  # 第 8 关
    {"move_char_time_ms": 10, "other_char": 5, "gen_char_time_ms": 300,
     "ball_color": yellow, "char_color": rainbow},  # 第 9 关
    {"move_char_time_ms": 10, "other_char": 8, "gen_char_time_ms": 250,
     "ball_color": "red", "char_color": rainbow},  # 第 10 关
]

win_size_map = [
    {'width': 800, 'height': 600, 'button_size': 20},
    {'width': 1024, 'height': 768, 'button_size': 30},
    {'width': 1366, 'height': 768, 'button_size': 30},
    {'width': 1440, 'height': 900, 'button_size': ''},
    {'width': 2560, 'height': 1600, 'button_size': ''},
    {'width': 2880, 'height': 1800, 'button_size': ''},
    {'width': 3072, 'height': 1920, 'button_size': ''},
    {'width': 2304, 'height': 1440, 'button_size': ''},
    {'width': 1920, 'height': 1080, 'button_size': ''},
    {'width': 5120, 'height': 2880, 'button_size': ''},
    {'width': 4096, 'height': 2304, 'button_size': ''},
    {'width': 1024, 'height': 768, 'button_size': ''},
    {'width': 3456, 'height': 2234, 'button_size': ''},
]
color_change = {
    '1': 'red',
    '2': 'blue',
    '3': yellow,
}
grade = 0
grade_map = grade_list[grade]

pause_button_text_color = 'gray'
continue_button_text_color = 'gray'

# 创建窗口
window = Tk()
window.title("打字游戏")
window.resizable(False, False)

# 获取屏幕的宽度和高度
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print(screen_width)
print(screen_height)
# screen_width = 1728
# screen_height = 1117
button_text_size = 30
# 计算窗口的坐标位置
window_width = screen_width * 7 // 10  # 窗口的宽度
window_height = int(screen_height * 8.4) // 10

# 窗口的高度
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 5  # 窗口的x坐标

# 设置窗口的位置和大小
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
canvas = Canvas(window, width=window_width, height=window_height)
canvas.config(bg='white')

canvas.pack()

is_continue = True
red_line_height = 20
red_line_x0 = 0
red_line_y0 = window_height - 80
red_line_x1 = window_width
red_line_y1 = red_line_y0

red_line = canvas.create_line(red_line_x0, red_line_y0, red_line_x1, red_line_y1,
                              fill='red', width=red_line_height)

ball_x1 = red_line_x1 // 2
ball_y1 = red_line_y1 - 45
ball_x1 = ball_x1 - 30 / 2
print(ball_x1)

print(f"ball_x1={ball_x1}|ball_y1={ball_y1}")
ball = ball_first(canvas, grade_map["ball_color"], ball_x1, ball_y1)

grade_label = Label(window, text="第 {} 关".format(grade + 1), font=("Arial", 30), bg='white')
score_label = Label(window, text="得分: 0", font=("Arial", 30), bg='white')

result_label = Label(window, text="你输了", font=("Arial", 100), bg='white', fg='red')
grade_label_width = grade_label.winfo_reqwidth()

grade_label_height = grade_label.winfo_reqheight()

score_label_width = score_label.winfo_reqwidth()
result_label_width = result_label.winfo_reqwidth()
result_label_height = result_label.winfo_reqheight()
gap_width = 20
grade_label_x = (window_width - grade_label_width - score_label_width - gap_width) // 2

grade_label.place(x=grade_label_x, y=10)
score = 0
score_label_x = grade_label_x + grade_label_width + gap_width

score_label.place(x=score_label_x, y=10)
result_label_x = (window_width - result_label_width) // 2
result_label_y = (window_height - result_label_height) // 2
result_label.place(x=result_label_x, y=result_label_y)

result_label.place_forget()
score2 = 0
is_game_over = False

quantity = 0
# music_ret_id_first = None
music_ret_id_mid = None

music_ret_id_last = None
# 创建一部字典来存储字母及其对应的标签
letters_tags = {}

matched_letters_set = set()


def is_match_color(item):
    char_color = canvas.itemcget(item, 'fill')
    ball_color = canvas.itemcget(ball, 'fill')
    if char_color == ball_color:
        return True
    else:
        return False


def get_text_color():
    char_color_str = grade_map['char_color']
    char_color_list = char_color_str.split(',')
    char_color = random.choice(char_color_list)
    return char_color


def generate_and_move():
    global task_id_generate_and_move, is_continue
    if not is_game_over and is_continue:
        value = choice(letters)
        random_x = randint(20, window_width - 20)
        text = canvas.create_text(random_x, grade_label_height + 40, text=value, font=("Arial", 24),
                                  fill=get_text_color())
        # 为每个字母分配一个唯一的标签
        unique_tag = str(uuid.uuid4())
        canvas.itemconfig(text, tags=(unique_tag,))
        # 将字母及其标签添加到字典中
        letters_tags[text] = unique_tag
        move_down(text)
        task_id_generate_and_move = window.after(grade_map["gen_char_time_ms"], generate_and_move)


def generate_extra_letters():
    global is_continue
    if is_continue:
        for _ in range(grade_map["other_char"]):
            value = choice(letters)
            random_x = randint(20, window_width - 20)
            text = canvas.create_text(random_x, grade_label_height + 40, text=value, font=("Arial", 24),
                                      fill=get_text_color())
            # 为每个字母分配一个唯一的标签
            unique_tag = str(uuid.uuid4())
            canvas.itemconfig(text, tags=(unique_tag,))
            # 将字母及其标签添加到字典中
            letters_tags[text] = unique_tag
            move_down(text)


def move_down(text):
    global score, score2, matched_letters_set, ball
    move_distance = 1
    if not is_continue:
        move_distance = 0
    if text not in matched_letters_set:
        canvas.move(text, 0, move_distance)
    coords_list = canvas.coords(text)
    if coords_list:
        if canvas.coords(text)[1] < red_line_y0 - red_line_height:
            window.after(grade_map["move_char_time_ms"], move_down, text)
        else:
            score2 += 1
            if score2 % 5 == 0:
                lost_game()
                ball = ball_first(canvas, grade_map["ball_color"], ball_x1, ball_y1)
            canvas.delete(text)
            canvas.update()
    else:
        canvas.delete(text)
        canvas.update()


def hit_text(text):
    target_x, target_y = get_text_center_coords(canvas, text)
    if target_x == -1 and target_y == -1:
        return
    ball_to(canvas, target_x, target_y, grade_map["ball_color"], pixel=10, sleep_ms=1,
            ball_x1=ball_x1, ball_y1=ball_y1)
    canvas.delete(text)


def is_color_change_key(key):
    return key in color_change


def do_color_change(key):
    color = color_change[key]
    grade_map["ball_color"] = color
    change_ball_color(canvas, ball, color)


def key_pressed(event):
    global score, quantity, matched_letters_set, ball
    if is_continue:
        key = event.char.upper()
        items = canvas.find_all()
        # 新增一个变量来记录是否找到未匹配的字母
        found_unmatched_letter = False
        for item in items:
            if is_color_change_key(key):
                do_color_change(key)
            if canvas.type(item) == 'text' and canvas.itemcget(item, 'text') == key and is_match_color(item):
                # 检查字母是否已经匹配
                if item not in matched_letters_set:
                    score += 1
                    quantity += 1
                    if quantity >= 4:
                        generate_extra_letters()
                        quantity = 0
                    if score >= (grade + 1) * 100:
                        winning_the_game()
                        ball = ball_first(canvas, grade_map["ball_color"], ball_x1, ball_y1)
                        quantity = 0
                    score_label.config(text=f"得分: {score}")
                    hit_text(item)
                    matched_letters_set.add(item)
                    if item in letters_tags:
                        del letters_tags[item]
                    found_unmatched_letter = True
                    canvas.update()
                    break

        # 如果未找到未匹配的字母，尝试从已匹配的字母集合中移除一个
        if not found_unmatched_letter:
            for letter in matched_letters_set.copy():
                if canvas.itemcget(letter, 'text') == key:
                    matched_letters_set.remove(letter)
                    break


task_id_generate_and_move = ""


def lost_game():
    global is_game_over, grade, grade_map, score, score2, red_line, music_ret_id_first, quantity
    is_game_over = True
    canvas.delete("all")
    make_red_line()
    result_label.place(x=result_label_x, y=result_label_y)
    if grade > 4:
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


def make_red_line():
    global red_line
    red_line = canvas.create_line(red_line_x0, red_line_y0, red_line_x1, red_line_y1,
                                  fill='red', width=red_line_height)


def winning_the_game():
    global is_game_over, grade, grade_map, music_ret_id_first, music_ret_id_mid, music_ret_id_last, \
        quantity, score, ball
    is_game_over = False
    # 增加关卡
    grade = grade + 1
    if grade == 10:
        grade = 0
        score = 0

    if grade == 0:
        music_ret_id_first = change_music(win, music_file_start, 290000,
                                          True, True, music_ret_id_last)
    elif grade == 5:
        music_ret_id_mid = change_music(win, music_file_mid, 620000,
                                        True, True, music_ret_id_first)
    elif grade == 8:
        music_ret_id_last = change_music(win, music_file_last, 79000,
                                         True, True, music_ret_id_mid)
    grade_map = grade_list[grade]

    ball = ball_first(canvas, grade_map["ball_color"], ball_x1, ball_y1)
    window.after(60, restart_game)
    canvas.update()


def restart_game():
    global score, score2, is_game_over, red_line, grade_map, quantity, ball
    is_game_over = False
    score2 = 0
    score_label.config(text=f"得分: {score} ")
    info = f"第 {grade + 1} 关"
    grade_label.config(text=info, font=("Arial", 30), bg='white', fg='black')
    window.after_cancel(task_id_generate_and_move)
    result_label.place_forget()
    canvas.delete("all")
    canvas.update()
    make_red_line()
    ball = ball_first(canvas, grade_map["ball_color"], ball_x1, ball_y1)
    quantity = 0
    generate_and_move()


def on_close():
    quit_music()
    win.destroy()
    window.destroy()


def close_game():
    on_close()


def start_game():
    global if_game_start
    if start_button.cget('fg') != 'gray':
        if_game_start = True
        generate_and_move()
        pause_button.config(fg='black')
        start_button.config(fg='gray')


def continue_game():
    global number, is_continue
    if continue_button.cget('fg') != 'gray':
        if number % 2 != 0:
            is_continue = True
            generate_and_move()
            pause_button.config(fg='black')
            continue_button.config(fg='gray')
            pygame.mixer.music.unpause()
            number += 1
        else:
            return
    else:
        return


def pause_game():
    global number, is_continue
    if pause_button.cget('fg') != 'gray':
        if number % 2 == 0:
            is_continue = False
            pygame.mixer.music.pause()
            pause_button.config(fg='gray')
            continue_button.config(fg='black')
            number += 1
        else:
            return
    else:
        return


def set_up():
    global number2, is_continue
    if set_up_button.cget('fg') != 'gray' and number % 2 == 0:
        set_up_button.config(fg='gray')
        is_continue = False

        def q():
            global is_continue, if_game_start
            if if_game_start:
                is_continue = True
                generate_and_move()
            new_window.destroy()
            set_up_button.config(fg='black')

        def on_window_close():
            set_up_button.config(fg='black')

        def on_scale_changed(value):
            # 将滑块值转换为音量（0 到 1 之间的浮点数）
            volume = float(value) / 10

            # 更新 Pygame 混音器的音量
            pygame.mixer.music.set_volume(volume)

        volume = round(pygame.mixer.music.get_volume(), 1)
        volume = volume * 10

        new_window = Toplevel(window)
        new_window.title("设置")
        new_window.protocol("WM_DELETE_WINDOW", on_window_close)
        new_window.resizable(False, False)
        new_window_height = screen_height // 2 // 2
        new_window_height = screen_height - new_window_height
        new_window.geometry(f'600x{new_window_height}')

        scale = Scale(new_window, from_=0, to=10, orient=HORIZONTAL, length=500, sliderlength=50, width=50,
                      command=on_scale_changed)
        scale.set(volume)
        scale.place(x=5, y=200)

        q_button = Button(new_window, text='退出设置', font=('Arial', 20), command=q)
        q_button.place(x=5, y=100)

        number2 += 1


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)


win = Tk()
music_file_start = resource_path("game_music_start.ogg")
music_file_mid = resource_path("game_music_mid_forever.mp3")
music_file_last = resource_path("game_music_last.mp3")

music_ret_id_first = play_music_by_window(win, music_file_start, 290000,
                                          True, True)
start_button = Button(canvas, text='开始', font=("Arial", button_text_size), fg='black', command=start_game)
start_width = start_button.winfo_reqwidth()
start_height = start_button.winfo_reqheight()

close_button = Button(canvas, text='退出', font=("Arial", button_text_size), command=close_game)
close_width = close_button.winfo_reqwidth()
close_height = close_button.winfo_reqheight()

pause_button = Button(canvas, text='暂停', font=("Arial", button_text_size), fg=pause_button_text_color,
                      command=pause_game)
pause_width = pause_button.winfo_reqwidth()
pause_height = pause_button.winfo_reqheight()

continue_button = Button(canvas, text='继续', font=("Arial", button_text_size), fg=continue_button_text_color,
                         command=continue_game)
continue_width = continue_button.winfo_reqwidth()
continue_height = continue_button.winfo_reqheight()

set_up_button = Button(canvas, text='设置', font=("Arial", button_text_size), command=set_up)
set_up_width = continue_button.winfo_reqwidth()
set_up_height = continue_button.winfo_reqheight()

button_width_gap = 40
button_height_gap = 22
start_x = (window_width - start_width - button_width_gap - close_width - button_width_gap
           - pause_width - button_width_gap - continue_width - button_width_gap - set_up_width) // 2
start_y = red_line_y0 + button_height_gap

close_x = start_x + start_width + button_width_gap
close_y = start_y

pause_x = close_x + close_width + button_width_gap
pause_y = start_y

continue_x = pause_x + pause_width + button_width_gap
continue_y = start_y

set_up_x = continue_x + continue_width + button_width_gap
set_up_y = start_y

start_button.place(x=start_x, y=start_y)
close_button.place(x=close_x, y=close_y)
pause_button.place(x=pause_x, y=pause_y)
continue_button.place(x=continue_x, y=continue_y)
set_up_button.place(x=set_up_x, y=set_up_y)

volume = round(pygame.mixer.music.get_volume(), 1)
print(f"Music volume: {volume}")

window.bind('<Key>', key_pressed)
window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()
