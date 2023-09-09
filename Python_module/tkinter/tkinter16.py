import uuid
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

# 创建窗口
window = Tk()
window.title("打字游戏")
window.resizable(False, False)

# 获取屏幕的宽度和高度
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# 计算窗口的坐标位置
window_width = 995  # 窗口的宽度
window_height = 800  # 窗口的高度
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2 - 10  # 窗口的x坐标

# 设置窗口的位置和大小
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

canvas = Canvas(window, width=window_width, height=window_height)
canvas.config(bg='white')
canvas.pack()

# ball_to(canvas, 900, 50, pixel=5, sleep_ms=1)
red_line_width = 20
red_line_x0 = 0
red_line_y0 = window_height - 50
red_line_x1 = window_width
red_line_y1 = red_line_y0
red_line = canvas.create_line(red_line_x0, red_line_y0, red_line_x1, red_line_y1,
                              fill='red', width=red_line_width)

grade_label = Label(window, text="第 {} 关".format(grade + 1), font=("Arial", 30), bg='white')
score_label = Label(window, text="得分: 0", font=("Arial", 30), bg='white')
result_label = Label(window, text="你输了", font=("Arial", 100), bg='white', fg='red')

grade_label_width = grade_label.winfo_reqwidth()
grade_label_height = grade_label.winfo_reqheight()

score_label_width = score_label.winfo_reqwidth()

result_label_width = result_label.winfo_reqwidth()
result_label_height = result_label.winfo_reqheight()
# print(f"result_label_width={result_label_width}|result_label_height={result_label_height}")
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

# 创建一个字典来存储字母及其对应的标签
letters_tags = {}
matched_letters_set = set()


def generate_and_move():
    global task_id_generate_and_move
    if not is_game_over:
        value = choice(letters)
        random_x = randint(20, window_width - 20)
        text = canvas.create_text(random_x, grade_label_height + 40, text=value, font=("Arial", 24), fill='black')

        # 为每个字母分配一个唯一的标签
        unique_tag = str(uuid.uuid4())
        canvas.itemconfig(text, tags=(unique_tag,))
        # 将字母及其标签添加到字典中
        letters_tags[text] = unique_tag

        move_down(text)
        task_id_generate_and_move = window.after(grade_map["down_speed"], generate_and_move)


def generate_extra_letters():
    for _ in range(grade_map["other_char"]):
        value = choice(letters)
        random_x = randint(20, window_width - 20)
        text = canvas.create_text(random_x, grade_label_height + 40, text=value, font=("Arial", 24), fill='black')

        # 为每个字母分配一个唯一的标签
        unique_tag = str(uuid.uuid4())
        canvas.itemconfig(text, tags=(unique_tag,))
        # 将字母及其标签添加到字典中
        letters_tags[text] = unique_tag

        move_down(text)


def move_down(text):
    global score, score2, matched_letters_set
    sleep = grade_map["sleep"]

    # 如果字母具有匹配的标签，则停止移动
    if text not in matched_letters_set:
        canvas.move(text, 0, 1)

    # y_speed = 1 + (600 - grade_map["down_speed"])
    # canvas.move(text, 0, 1)
    coords_list = canvas.coords(text)
    # print(f"text={text}|coords_list={coords_list}")
    if coords_list:
        if canvas.coords(text)[1] < 730:
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
    global score, quantity, matched_letters_set
    key = event.char.upper()
    items = canvas.find_all()

    # 新增一个变量来记录是否找到未匹配的字母
    found_unmatched_letter = False

    for item in items:
        if canvas.type(item) == 'text' and canvas.itemcget(item, 'text') == key:
            # 检查字母是否已经匹配
            if item not in matched_letters_set:
                score += 1
                quantity += 1
                if quantity >= 4:
                    generate_extra_letters()
                    quantity = 0
                if score >= (grade + 1) * 100:
                    winning_the_game()
                    quantity = 0
                score_label.config(text=f"得分: {score}")

                matched_letters_set.add(item)
                del letters_tags[item]
                found_unmatched_letter = True
                canvas.update()
                # canvas.delete(item)

                # 为匹配的字母添加"matched"标签
                # canvas.itemconfig(item, tags=("matched",))
                # items.remove(item)
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


def make_red_line():
    global red_line
    red_line = canvas.create_line(red_line_x0, red_line_y0, red_line_x1, red_line_y1,
                                  fill='red', width=red_line_width)


def winning_the_game():
    global is_game_over, grade, grade_map, music_ret_id_first, music_ret_id_mid, music_ret_id_last, quantity, score
    is_game_over = False
    # canvas.delete("all")
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

    window.after(60, restart_game)
    canvas.update()


def restart_game():
    global score, score2, is_game_over, red_line, grade_map, quantity
    # score = 0
    is_game_over = False
    score2 = 0
    score_label.config(text=f"得分: {score} ")
    info = f"第 {grade + 1} 关"
    # info = f"第 {grade + 1} 关 ->参数:{grade_map}, quantity: {quantity}"
    grade_label.config(text=info, font=("Arial", 30), bg='white', fg='black')
    window.after_cancel(task_id_generate_and_move)
    result_label.place_forget()

    canvas.delete("all")
    canvas.update()

    make_red_line()
    quantity = 0
    generate_and_move()
    # print(f"restart_game_quantity={quantity}")


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
