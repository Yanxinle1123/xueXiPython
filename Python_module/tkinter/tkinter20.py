from comm.common import rgb_to_hex


# window = tk.Tk()
# window.resizable(False, False)


def ball_to(canvas, target_x, target_y, ball_color='#75147b', pixel=0.1, ball_x1=485,
            ball_y1=700,
            ball_x2=515, ball_y2=730, sleep_ms=1):
    def contains_digit(s):
        return any(char.isdigit() for char in s)

    # canvas = tk.Canvas(win, width=width, height=height)
    # canvas.pack()

    hex1 = ball_color
    num = contains_digit(hex1)
    if hex1[0] != '#' and num:
        hex1 = hex1.upper()
        hex2 = rgb_to_hex(hex1)
    else:
        hex2 = hex1

    # 画第一个圆形
    canvas.create_oval(ball_x1, ball_y1, ball_x2, ball_y2, fill=hex2)

    # 画第一个圆形
    purple_ball2 = canvas.create_oval(ball_x1, ball_y1, ball_x2, ball_y2, fill=hex2)

    # 计算紫球的中心坐标
    global purple_center_x, purple_center_y
    purple_center_x, purple_center_y = (ball_x1 + ball_x2) / 2, (ball_y1 + ball_y2) / 2

    # 定义移动紫球的函数
    def move_purple_ball():
        global purple_center_x, purple_center_y

        # 计算与目标位置的剩余距离
        remaining_distance_x, remaining_distance_y = target_x - purple_center_x, target_y - purple_center_y

        # 使用线性插值算法计算移动步长
        lerp_factor = min(pixel / ((remaining_distance_x ** 2 + remaining_distance_y ** 2) ** 0.5), 1)
        move_dx = lerp_factor * remaining_distance_x
        move_dy = lerp_factor * remaining_distance_y

        # 移动紫球
        canvas.move(purple_ball2, move_dx, move_dy)

        # 更新紫球的中心坐标
        purple_center_x += move_dx
        purple_center_y += move_dy

        # 判断是否到达目标位置
        if lerp_factor == 1:
            # 停止移动
            return

        # 延迟一段时间后再次调用move_purple_ball()函数
        canvas.after(sleep_ms, move_purple_ball)

    # 调用move_purple_ball()函数，开始移动紫球
    move_purple_ball()

    # win.mainloop()

# if __name__ == '__main__':
#     ball_to(window, 900, 50, pixel=5, sleep_ms=1)
