import os
import random
import sys
import tkinter.font as tkfont
import uuid
from random import randint, choice
from tkinter import Tk, Canvas, Label, Button, Toplevel, HORIZONTAL, Scale

import pygame

from comm.comm_draw import ball_to, get_text_center_coords, ball_first, change_ball_color
from comm.comm_music import play_music_by_window, quit_music, change_music

# if not sys.stdout:
#     sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)

number = 0
number2 = 0
if_start_game = False
if_pause_game = False
ball_speed = 8
value_list = []

yellow = 'green'
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

rainbow = f'red,blue,{yellow}'
two_color = "red,blue"
button_color = 'lower'

lower_list = [
    {"move_char_time_ms": 20, "other_char": 0, "gen_char_time_ms": 500,
     "ball_color": "red", "char_color": "red"},  # 第 1 关
    {"move_char_time_ms": 15, "other_char": 0, "gen_char_time_ms": 500,
     "ball_color": "red", "char_color": "red"},  # 第 2 关
    {"move_char_time_ms": 10, "other_char": 0, "gen_char_time_ms": 600,
     "ball_color": "blue", "char_color": "blue"},  # 第 3 关
    {"move_char_time_ms": 20, "other_char": 2, "gen_char_time_ms": 400,
     "ball_color": "green", "char_color": yellow},  # 第 4 关
    {"move_char_time_ms": 20, "other_char": 2, "gen_char_time_ms": 300,
     "ball_color": "red", "char_color": two_color},  # 第 5 关
    {"move_char_time_ms": 20, "other_char": 5, "gen_char_time_ms": 200,
     "ball_color": "red", "char_color": rainbow},  # 第 6 关
    {"move_char_time_ms": 10, "other_char": 3, "gen_char_time_ms": 200,
     "ball_color": yellow, "char_color": f"{yellow},red"},  # 第 7 关
    {"move_char_time_ms": 20, "other_char": 3, "gen_char_time_ms": 400,
     "ball_color": "blue", "char_color": rainbow},  # 第 8 关
    {"move_char_time_ms": 15, "other_char": 5, "gen_char_time_ms": 300,
     "ball_color": yellow, "char_color": rainbow},  # 第 9 关
    {"move_char_time_ms": 10, "other_char": 8, "gen_char_time_ms": 250,
     "ball_color": "red", "char_color": rainbow},  # 第 10 关
]

medium_list = [
    {"move_char_time_ms": 15, "other_char": 2, "gen_char_time_ms": 400,
     "ball_color": "red", "char_color": "red"},  # 第 1 关
    {"move_char_time_ms": 10, "other_char": 2, "gen_char_time_ms": 500,
     "ball_color": "red", "char_color": "red"},  # 第 2 关
    {"move_char_time_ms": 10, "other_char": 2, "gen_char_time_ms": 500,
     "ball_color": "blue", "char_color": "blue"},  # 第 3 关
    {"move_char_time_ms": 15, "other_char": 2, "gen_char_time_ms": 400,
     "ball_color": "green", "char_color": yellow},  # 第 4 关
    {"move_char_time_ms": 15, "other_char": 2, "gen_char_time_ms": 300,
     "ball_color": "red", "char_color": two_color},  # 第 5 关
    {"move_char_time_ms": 15, "other_char": 5, "gen_char_time_ms": 200,
     "ball_color": "red", "char_color": rainbow},  # 第 6 关
    {"move_char_time_ms": 10, "other_char": 3, "gen_char_time_ms": 200,
     "ball_color": yellow, "char_color": f"{yellow},red"},  # 第 7 关
    {"move_char_time_ms": 15, "other_char": 3, "gen_char_time_ms": 400,
     "ball_color": "blue", "char_color": rainbow},  # 第 8 关
    {"move_char_time_ms": 10, "other_char": 5, "gen_char_time_ms": 300,
     "ball_color": yellow, "char_color": rainbow},  # 第 9 关
    {"move_char_time_ms": 10, "other_char": 8, "gen_char_time_ms": 250,
     "ball_color": "red", "char_color": rainbow},  # 第 10 关
]

advanced_list = [
    {"move_char_time_ms": 15, "other_char": 5, "gen_char_time_ms": 400,
     "ball_color": "red", "char_color": "red"},  # 第 1 关
    {"move_char_time_ms": 10, "other_char": 5, "gen_char_time_ms": 500,
     "ball_color": "red", "char_color": "red"},  # 第 2 关
    {"move_char_time_ms": 10, "other_char": 5, "gen_char_time_ms": 500,
     "ball_color": "blue", "char_color": "blue"},  # 第 3 关
    {"move_char_time_ms": 15, "other_char": 7, "gen_char_time_ms": 400,
     "ball_color": "green", "char_color": yellow},  # 第 4 关
    {"move_char_time_ms": 15, "other_char": 7, "gen_char_time_ms": 300,
     "ball_color": "red", "char_color": two_color},  # 第 5 关
    {"move_char_time_ms": 15, "other_char": 10, "gen_char_time_ms": 200,
     "ball_color": "red", "char_color": rainbow},  # 第 6 关
    {"move_char_time_ms": 10, "other_char": 8, "gen_char_time_ms": 200,
     "ball_color": yellow, "char_color": f"{yellow},red"},  # 第 7 关
    {"move_char_time_ms": 15, "other_char": 8, "gen_char_time_ms": 400,
     "ball_color": "blue", "char_color": rainbow},  # 第 8 关
    {"move_char_time_ms": 10, "other_char": 10, "gen_char_time_ms": 300,
     "ball_color": yellow, "char_color": rainbow},  # 第 9 关
    {"move_char_time_ms": 10, "other_char": 8, "gen_char_time_ms": 200,
     "ball_color": "red", "char_color": rainbow},  # 第 10 关
]

what_list = lower_list

# win_size_map = [
#     {'width': 800, 'height': 600, 'button_size': 20},
#     {'width': 1024, 'height': 768, 'button_size': 30},
#     {'width': 1366, 'height': 768, 'button_size': 30},
#     {'width': 1440, 'height': 900, 'button_size': ''},
#     {'width': 2560, 'height': 1600, 'button_size': ''},
#     {'width': 2880, 'height': 1800, 'button_size': ''},
#     {'width': 3072, 'height': 1920, 'button_size': ''},
#     {'width': 2304, 'height': 1440, 'button_size': ''},
#     {'width': 1920, 'height': 1080, 'button_size': ''},
#     {'width': 5120, 'height': 2880, 'button_size': ''},
#     {'width': 4096, 'height': 2304, 'button_size': ''},
#     {'width': 1024, 'height': 768, 'button_size': ''},
#     {'width': 3456, 'height': 2234, 'button_size': ''},
# ]
color_change = {
    '1': 'red',
    '2': 'blue',
    '3': yellow,
}
key_color = {
    'red': [],
    'blue': [],
    yellow: []
}
random_char_config = {
    'red': {'random_count': 2, 'freeze_time': 0},
    'blue': {'random_count': 0, 'freeze_time': 1},
    yellow: {'random_count': 5, 'freeze_time': 0},
}
key_color_index = 0
grade = 0
grade_map = what_list[grade]

pause_button_text_color = 'gray'
continue_button_text_color = 'gray'

# 创建窗口
window = Tk()
window.title("打字游戏")
window.resizable(False, False)

# 获取屏幕的宽度和高度
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# print(screen_width)
# print(screen_height)
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
# print(ball_x1)

# print(f"ball_x1={ball_x1}|ball_y1={ball_y1}")
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


def add_fixed_list(value_list_var, text, size=10):
    global key_color_index
    list_size = len(value_list_var)
    if list_size < size:
        value_list_var.append(text)
    else:
        value_list_var[key_color_index] = text
        key_color_index = (key_color_index + 1) % size
    return value_list_var


def generate_and_move():
    global task_id_generate_and_move, is_continue, value_list
    if not is_game_over and is_continue:
        value = choice(letters)
        random_x = randint(20, window_width - 20)
        char_color = get_text_color()
        text = canvas.create_text(random_x, grade_label_height + 40, text=value, font=("Arial", 24),
                                  fill=char_color)
        # 为每个字母分配一个唯一的标签
        unique_tag = str(uuid.uuid4())
        canvas.itemconfig(text, tags=(unique_tag,))
        # 将字母及其标签添加到字典中
        letters_tags[text] = unique_tag
        value_list = key_color[char_color]
        add_fixed_list(value_list, text, size=100)
        # print(f'value_list = {value_list}')
        # print(f'char_color = {char_color}')
        # print(f'key_color = {key_color}')
        # print(f'text = {text}')
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


is_freeze_var = False


def is_freeze():
    return is_freeze_var


def set_freeze(freeze_var):
    global is_freeze_var
    is_freeze_var = freeze_var


def move_down(text):
    global score, score2, matched_letters_set, ball, is_continue
    move_distance = 1
    if not is_continue or is_freeze():
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
    ball_color = grade_map["ball_color"]
    ball_to(canvas, target_x, target_y, ball_color, pixel=ball_speed, sleep_ms=1,
            ball_x1=ball_x1, ball_y1=ball_y1, text=text)
    magic_ball(canvas, ball_color)


def is_color_change_key(key):
    return key in color_change


def do_color_change(key):
    color = color_change[key]
    grade_map["ball_color"] = color
    change_ball_color(canvas, ball, color)


def key_pressed(event):
    global score, quantity, matched_letters_set, ball, value_list
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
                    if item in value_list:
                        value_list.remove(item)
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
    grade_map = what_list[grade]

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
    grade_map = what_list[grade]

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
    global if_start_game, is_continue
    if start_button.cget('fg') != 'gray':
        if_start_game = True
        is_continue = True
        generate_and_move()
        pause_button.config(fg='black')
        start_button.config(fg='gray')


def continue_game():
    global number, is_continue, if_pause_game
    if continue_button.cget('fg') != 'gray':
        if number % 2 != 0:
            is_continue = True
            if_pause_game = False
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
    global number, is_continue, if_pause_game
    if pause_button.cget('fg') != 'gray':
        if number % 2 == 0:
            if_pause_game = True
            is_continue = False
            pygame.mixer.music.pause()
            pause_button.config(fg='gray')
            continue_button.config(fg='black')
            number += 1
        else:
            return
    else:
        return


def magic_ball(canvas_var, magic_ball_color):
    global score, value_list
    value_list2 = key_color[magic_ball_color]
    random_config = random_char_config[magic_ball_color]
    random_count = random_config['random_count']
    freeze_time = random_config['freeze_time']
    random_char_color_count = min(random_count, len(value_list2))
    choice_char_list = []
    choice_char_list.extend(random.sample(value_list2, random_char_color_count))
    for one in choice_char_list:
        canvas_var.delete(one)
        canvas_var.update()
        if one in value_list:
            value_list.remove(one)
    if freeze_time > 0:
        set_freeze(True)
        canvas_var.after(freeze_time * 1000, set_freeze, False)


def set_up():
    global number2, is_continue, ball_speed, what_list
    if set_up_button.cget('fg') != 'gray' and number2 % 2 == 0:
        set_up_button.config(fg='gray')
        is_continue = False
        pygame.mixer.music.unpause()

        def quit_set_up():
            global is_continue, if_start_game, if_pause_game, number2, ball_speed
            if if_start_game and if_pause_game:
                pygame.mixer.music.pause()
                pygame.mixer.music.set_volume(volume_var)
                is_continue = False
            if if_start_game and not if_pause_game:
                is_continue = True
                generate_and_move()
            new_window.destroy()
            set_up_button.config(fg='black')
            number2 += 1

        def on_scale_changed(value):
            # 将滑块值转换为音量（0 到 1 之间的浮点数）
            volume_var2 = float(value) / 10

            # 更新 Pygame 混音器的音量
            pygame.mixer.music.set_volume(volume_var2)

        def ball_speed_function(value):
            global ball_speed
            ball_speed = int(value) + 8

        def this_lower_list():
            global what_list, grade_map, button_color
            what_list = lower_list
            grade_map = what_list[grade]
            lower_game_button.config(fg='red')
            medium_game_button.config(fg='black')
            advanced_game_button.config(fg='black')
            button_color = 'lower'

        def this_medium_list():
            global what_list, grade_map, button_color
            what_list = medium_list
            grade_map = what_list[grade]
            lower_game_button.config(fg='black')
            medium_game_button.config(fg='red')
            advanced_game_button.config(fg='black')
            button_color = 'medium'

        def this_advanced_list():
            global what_list, grade_map, button_color
            what_list = advanced_list
            grade_map = what_list[grade]
            lower_game_button.config(fg='black')
            medium_game_button.config(fg='black')
            advanced_game_button.config(fg='red')
            button_color = 'advanced'

        def button_color_function():
            global button_color
            if button_color == 'lower':
                lower_game_button.config(fg='red')
            elif button_color == 'medium':
                medium_game_button.config(fg='red')
            else:
                advanced_game_button.config(fg='red')

        volume_var = round(pygame.mixer.music.get_volume(), 1) * 10

        new_window = Toplevel(window)
        new_window.title("设置")
        new_window.protocol("WM_DELETE_WINDOW", quit_set_up)
        new_window.resizable(False, False)
        new_window.update_idletasks()

        new_window_height = int(screen_height * 0.75)
        new_window_width = int(screen_width * 0.3)
        new_window.geometry(f'{new_window_width}x{new_window_height}')

        music_label = Label(new_window, text='音乐音量', font=('Arial', 20))
        music_label_height = music_label.winfo_reqheight()
        # print(f"music_label_width={music_label_width}|music_label_height={music_label_height}")

        scale_len = int(new_window_width * 0.95)
        scale_width = 40
        scale_height = 20

        scale_music = Scale(new_window, from_=0, to=10, orient=HORIZONTAL,
                            length=scale_len, sliderlength=scale_width, width=scale_width,
                            command=on_scale_changed)
        scale_music_length = scale_music.cget("length")
        scale_music_width = scale_music.cget("width")
        # print(f"scale_music_length={scale_music_length}|scale_music_width={scale_music_width}")
        scale_music_x = new_window_width // 2 - scale_music_length // 2
        scale_music_y = music_label_height + scale_height
        scale_music.set(volume_var)
        scale_music.place(x=scale_music_x, y=scale_music_y)

        ball_speed_label = Label(new_window, text='球的速度', font=('Arial', 20))
        scale_ball_speed = Scale(new_window, from_=1, to=10, orient=HORIZONTAL,
                                 length=scale_len, sliderlength=scale_width, width=scale_width,
                                 command=ball_speed_function)
        # print(f"scale_ball_speed_length={scale_ball_speed_length}|scale_ball_speed_width={scale_ball_speed_width}")
        scale_ball_speed_x = scale_music_x
        scale_ball_speed_y = scale_music_y + scale_music_width + music_label_height + scale_height * 3
        scale_ball_speed.place(x=scale_ball_speed_x, y=scale_ball_speed_y)

        game_difficult_label = Label(new_window, text='游戏难度', font=('Arial', 20))

        lower_game_button = Button(new_window, text='低等难度', font=('Arial', 50), command=this_lower_list)
        medium_game_button = Button(new_window, text='中等难度', font=('Arial', 50), command=this_medium_list)
        advanced_game_button = Button(new_window, text='高等难度', font=('Arial', 50), command=this_advanced_list)

        lower_game_button_width = lower_game_button.winfo_reqwidth()
        medium_game_button_width = medium_game_button.winfo_reqwidth()
        advanced_game_button_width = advanced_game_button.winfo_reqwidth()
        lower_game_button_x = new_window_width // 2 - lower_game_button_width // 2
        medium_game_button_x = new_window_width // 2 - medium_game_button_width // 2
        advanced_game_button_x = new_window_width // 2 - advanced_game_button_width // 2

        # music_label_width = music_label.winfo_width()
        music_label_font = tkfont.Font(font=music_label['font'])
        music_label_width = music_label_font.measure('音乐音量 ')
        ball_speed_label_font = tkfont.Font(font=music_label['font'])
        ball_speed_label_width = ball_speed_label_font.measure('球的速度 ')
        that_list_label_font = tkfont.Font(font=game_difficult_label['font'])
        that_list_label_width = that_list_label_font.measure('游戏难度 ')

        quit_button = Button(new_window, text='退出设置', font=('Arial', 50), command=quit_set_up)
        quit_button_width = quit_button.winfo_reqwidth()
        quit_button_height = quit_button.winfo_reqheight()
        quit_button_x = new_window_width // 2 - quit_button_width // 2
        quit_button_y = new_window_height - (quit_button_height + quit_button_height // 2)
        quit_button.place(x=quit_button_x, y=quit_button_y)

        # 使用 Font 对象的 metrics() 方法获取 Label 的高度
        music_label_height = music_label_font.metrics("linespace")
        music_label_x = new_window_width // 2 - music_label_width // 2
        ball_speed_label_x = new_window_width // 2 - ball_speed_label_width // 2
        music_label_y = music_label_height
        that_list_label_x = new_window_width // 2 - that_list_label_width // 2
        music_label.place(x=music_label_x, y=music_label_y)
        ball_speed_label.place(x=ball_speed_label_x, y=150)
        scale_ball_speed.set(ball_speed - 8)
        game_difficult_label.place(x=that_list_label_x, y=280)
        lower_game_button.place(x=lower_game_button_x, y=350)
        medium_game_button.place(x=medium_game_button_x, y=450)
        advanced_game_button.place(x=advanced_game_button_x, y=550)
        button_color_function()
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
# print(f"Music volume: {volume}")

window.bind('<Key>', key_pressed)
window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()
